import pandas as pd
import os
import math

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from utils.converter import h5_to_dict

OUTPUT_CSV_PATH = "data/songs.csv"
INPUT_FILE_PATH = "data/MillionSongSubset"

try:
    # Attempt to import data if it already exists
    df = pd.read_csv("data/songs.csv")
except:
    # Convert HDF5 files into a pandas dataframe.
    rows = []

    for root, _, files in os.walk(INPUT_FILE_PATH):
        for file in files:
            h5_path = os.path.join(root, file)
            try:
                song_data = h5_to_dict(h5_path)
                rows.append(song_data)
            except Exception as e:
                print(f"Error loading file {file}: {e}")

    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT_CSV_PATH, index=False)

print(f"CSV created: {OUTPUT_CSV_PATH}")

# Reshape Taste Profile subset
temp_df = pd.read_csv(
    "data/train_triplets.txt",
    delimiter="\t",
    names=["user_id", "song_id", "play_count"],
)
temp_df = temp_df.sort_values(by=["user_id", "play_count"], ascending=[True, False])

# Only use a subset of the data
temp_df = temp_df.head(math.floor(len(temp_df.index) * 0.01))
temp_df.head()

# Assign an index to every unique song in the list
codes, unique = pd.factorize(temp_df["song_id"])
temp_df["song_id_coded"] = pd.to_numeric(codes)

# Get some useful stats
num_songs = len(unique)
num_users = len(temp_df["user_id"].value_counts().keys())

# Find top 5 songs
top_songs = temp_df.groupby("user_id").head(5)
taste_profile_df = (
    top_songs.groupby("user_id")["song_id_coded"].apply(list).reset_index()
)
taste_profile_df.columns = ["user", "top_5_song_id_coded"]
taste_profile_df[[f"track_{i}_coded" for i in range(1, 6)]] = pd.DataFrame(
    taste_profile_df[f"top_5_song_id_coded"].to_list(), index=taste_profile_df.index
)

print(f"There are {num_songs} songs and {num_users} users in our selection.")

taste_profile_df.to_csv("data/taste_profile.csv", index=False)
taste_profile_df.head(10)

# Create one-hot encoding vectors
encoder = OneHotEncoder(sparse_output=False)
encoder.set_output(transform="pandas")

df_encoded_keys = encoder.fit_transform(df[["analysis/songs/key"]])
df_encoded_mode = encoder.fit_transform(df[["analysis/songs/mode"]])

df = pd.concat([df, df_encoded_keys, df_encoded_mode], axis=1)

# Apply the StandardScaler to normalize datapoints in the tempo column using Z-score distribution
scaler = StandardScaler()

df["analysis/songs/tempo"] = scaler.fit_transform(df[["analysis/songs/tempo"]])
df["analysis/songs/loudness"] = scaler.fit_transform(df[["analysis/songs/loudness"]])
df["analysis/songs/duration"] = scaler.fit_transform(df[["analysis/songs/duration"]])
