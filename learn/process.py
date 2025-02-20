import torch

from torch import nn
from random import randint
from preprocess import taste_profile_df, num_songs, num_users
from models.models import SongEmbeddingModel

device = (
    torch.accelerator.current_accelerator().type
    if torch.accelerator.is_available()
    else "cpu"
)
print(f"Using {device} device")

input_len = 4  # The number of favourite songs considered as input for each user
embedding_dim = 3

columns = [f"track_{i}_coded" for i in range(1, input_len + 1)]
target = nn.functional.one_hot(
    torch.tensor(taste_profile_df[f"track_{input_len + 1}_coded"].to_numpy()),
    num_classes=num_songs,
).to(dtype=torch.float)
model_input = torch.tensor(taste_profile_df[columns].to_numpy())

print("Checking target one hot encodings at random...")
passes = 0
num_tests = 10
for idx in range(num_tests):
    x = randint(0, num_users)
    y = randint(0, num_songs)
    expected = 1 if taste_profile_df.iloc[x][f"track_{input_len + 1}_coded"] == y else 0
    song_id = taste_profile_df.iloc[x][f"track_{input_len + 1}_coded"]

    if target[x][y].item() == expected and target[x][song_id].item() == 1:
        print(f"{idx}: OK")
        passes += 1
    else:
        print(f"{idx}: FAIL {target[x][y].item(), expected} {x, song_id}")

print(f"{passes} of {num_tests} tests passed.")

model = SongEmbeddingModel(embedding_dim, input_len, target)
output = model(model_input)
