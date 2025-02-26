import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F
import threading
import queue

from torch import nn, optim
from random import randint
from models.models import RecommendationModel
from preprocess import taste_profile_df, track_cols, num_songs, num_users
from matplotlib.animation import FuncAnimation

# Creating target tensors for training the model
# Single-label targets where we try to predict the last track in the user's list of top n tracks
target_s = F.one_hot(
    torch.tensor(taste_profile_df[f"track_{len(track_cols)}_coded"].to_numpy()),
    num_classes=num_songs,
).type(torch.float32)

# Multi-label targets where we try to predict all of the user's top n tracks
tracks = torch.tensor(taste_profile_df[track_cols].to_numpy())

# Creates a matrix filled with zeroes of the size (num_users x num_songs),
# then fills it in with 1s based on the indices given in tracks.
# THIS WILL ONLY WORK CORRECTLY IF THE SONGS ARE ENCODED STRICTLY FROM 0 TO num_songs - 1
target_m = torch.zeros(num_users, num_songs).scatter_(1, tracks, 1.0)

model_input = torch.tensor(taste_profile_df[track_cols[:-1]].to_numpy())

passes = 0
num_tests = 10000
for idx in range(num_tests):
    # Select a random user and a random song
    x = randint(0, num_users - 1)
    y = randint(0, num_songs - 1)
    z = randint(1, len(track_cols))

    # Expect 1 if the randomly selected user has the randomy selected song in their top 5
    expected_s = (
        1 if taste_profile_df.iloc[x][f"track_{len(track_cols)}_coded"] == y else 0
    )
    # At the same time, find out what song the randomly selected user actually likes
    song_id_s = taste_profile_df.iloc[x][f"track_{len(track_cols)}_coded"]
    song_id_m = taste_profile_df.iloc[x][f"track_{z}_coded"]

    cond_expected_s = (
        target_s[x][y].item() == expected_s and target_s[x][song_id_s].item() == 1
    )
    cond_expected_m = target_m[x][song_id_m].item() == 1

    if cond_expected_s:
        passes += 1

print(f"{passes} of {num_tests} tests passed.")
if passes < num_tests:
    print("Do not proceed with training.")

device = (
    torch.accelerator.current_accelerator().type
    if torch.accelerator.is_available()
    else "cpu"
)
print(f"Using {device} device")

input_len = 4  # The number of favourite songs considered as input for each user
embedding_dim = 3

model = RecommendationModel(num_songs, embedding_dim)

loss_fn = nn.BCEWithLogitsLoss()
lr = 0.001
optimizer = optim.Adam(model.parameters(), lr=lr)

n_epochs = 100
batch_size = 10

fig, ax = plt.subplots()
x_data, y_data = [], []
(line,) = ax.plot([], [], "r-", lw=2)
loss_start = -1
loss_queue = queue.Queue()

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel("Epochs")
ax.set_ylabel("Loss")


def update(frame):
    while not loss_queue.empty():
        loss = loss_queue.get()

        x_data.append(len(y_data))
        y_data.append(loss)
        line.set_data(x_data, y_data)

        # Adjust x-limits dynamically
        ax.set_xlim(0, x_data[-1] + 1)
        ax.set_ylim(0, max(y_data[-1], loss_start))

    return (line,)


def train():
    global loss_start
    global loss_queue

    for _ in range(n_epochs):
        for i in range(0, len(model_input), batch_size):
            batch = model_input[i : i + batch_size]
            y_pred = model(batch)
            y_batch = target_m[i : i + batch_size]
            loss = loss_fn(y_pred, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        loss_queue.put(loss.item())
        if loss_start == -1:
            loss_start = loss.item()


train_thread = threading.Thread(target=train, daemon=True)
train_thread.start()

ani = FuncAnimation(fig, update, frames=range(n_epochs), interval=100, blit=True)
plt.show()
