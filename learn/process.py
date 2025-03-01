import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F
import queue

from torch import nn, optim
from random import randint
from learn.models import RecommendationModel
from preprocess import taste_profile_df, track_cols, num_songs, num_users
from IPython.display import display, clear_output

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

# loss_fn = nn.BCEWithLogitsLoss()
loss_fn = nn.BCEWithLogitsLoss(reduction="none")
lr = 0.001
optimizer = optim.Adam(model.parameters(), lr=lr)

n_epochs = 500
batch_size = 10

fig, ax = plt.subplots()
x_data, y_data = [], []
(line,) = ax.plot(x_data, y_data, "r-", lw=2)
loss_upper = 0
loss_lower = 1
loss_queue = queue.Queue()

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel("Epochs")
ax.set_ylabel("Loss")
ax.set_title("Loss Curve")
ax.xaxis.get_major_locator().set_params(integer=True)

# Create weights
weights = torch.ones(num_users, num_songs)
weights.scatter_(1, tracks[:, -1].unsqueeze(1), 2.0)

for epoch in range(n_epochs):
    for i in range(0, len(model_input), batch_size):
        batch = model_input[i : i + batch_size]
        y_pred = model(batch)
        y_batch = target_m[i : i + batch_size]
        weights_batch = weights[i : i + batch_size]

        # loss = loss_fn(y_pred, y_batch)
        loss_per_element = loss_fn(y_pred, y_batch)
        weighted_loss = loss_per_element * weights_batch
        loss = weighted_loss.mean()

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Update plot
    loss_val = loss.item()
    x_data.append(epoch)
    y_data.append(loss_val)
    line.set_data(x_data, y_data)

    loss_lower = min(loss_lower, loss_val)
    loss_upper = max(loss_upper, loss_val)
    loss_range = loss_upper - loss_lower
    ax.set_xlim(0, x_data[-1] + 1)
    if loss_lower != loss_upper:
        ax.set_ylim(
            max(0, loss_lower - loss_range * 0.1), min(1, loss_upper + loss_range * 0.1)
        )
    else:
        ax.set_ylim(0, 1)

    clear_output(wait=True)
    display(fig)

print("Done.")

torch.save(model.state_dict(), "data/recommender.pt")
print(
    f"Model saved. (Number of songs: {num_songs}, Embedding Dimensions: {embedding_dim})"
)
