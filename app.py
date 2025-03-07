import os
import torch
import sqlite3
import string
import random

from learn.models import RecommendationModel
from fastapi import Request, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
print(os.getenv("REDIRECT_URI"))

app = FastAPI()

# Loading the model
model = RecommendationModel(74581, 3)
model.load_state_dict(torch.load("data/recommender.pt", weights_only=False))

# Opening a database connection
conn = sqlite3.connect("data/track_metadata.db")
cursor = conn.cursor()


# Getting authorization
@app.get("/authorize")
def authorize():
    query = {
        "client_id": os.getenv("CLIENT_ID"),
        "response_type": "token",
        "redirect_uri": os.getenv("REDIRECT_URI"),
        "state": "".join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            for _ in range(16)
        ),
    }

    query_str = urlencode(query)
    return RedirectResponse(url=f"https://accounts.spotify.com/authorize?{query_str}")


@app.get("/songs")
async def get_random_songs(random: bool = True, limit: int = 10):
    cursor.execute(
        f"""
        SELECT *
        FROM song_codes
        JOIN songs USING (song_id)
        {'ORDER BY random()' if random else ''}
        LIMIT {limit};
        """
    )

    songs = []
    rows = cursor.fetchall()
    cols = cursor.description
    for row in rows:
        song = {}
        for k, v in zip(cols, row):
            song[k[0]] = v
        songs.append(song)

    return {"songs": songs}


def get_song_metadata(id):
    """Return a song's metadata by its ID"""

    cursor.execute("SELECT * FROM songs WHERE song_id = (?)", (id,))
    rows = cursor.fetchall()
    cols = cursor.description

    if len(rows) > 0:
        song = {}
        for k, v in zip(cols, rows[0]):
            song[k[0]] = v
        return song
    else:
        raise HTTPException(status_code=400, detail=f"No song with ID - {id}")


def get_song_code(id):
    """Return a song's code by its ID"""

    cursor.execute('SELECT "index" FROM song_codes WHERE song_id = (?)', (id,))
    rows = cursor.fetchall()

    if len(rows) > 0:
        return int(rows[0][0])
    else:
        raise HTTPException(status_code=400, detail=f"No song with ID - {id}")


@app.get("/preview")
def get_preview(title: str):
    pass


@app.get("/song/{id}")
async def get_song(id):
    return get_song_metadata(id)


@app.post("/predict")
async def predict(request: Request):
    body = await request.json()
    if len(body["profile"]) != 4:
        raise HTTPException(status_code=400, detail="Profile length must be equal to 4")
    else:
        profile = []
        limit = body["limit"]

        for song_id in body["profile"]:
            song_code = get_song_code(song_id)
            profile.append(song_code)

        if limit < 2:
            raise HTTPException(status_code=400, detail="Limit cannot be lesser than 2")

        logits = model(torch.tensor(profile).unsqueeze(0))
        probabilities = torch.sigmoid(logits)
        topk_probabilities = torch.topk(probabilities, limit)

        # print(profile)
        # print(topk_probabilities)

        recommendations = {}
        for i, val in zip(
            topk_probabilities.indices.squeeze().tolist(),
            topk_probabilities.values.squeeze().tolist(),
        ):
            cursor.execute('SELECT * FROM song_codes WHERE "index" = (?)', (i,))
            song_id = cursor.fetchall()[0][1]
            recommendations[song_id] = val

        return recommendations
