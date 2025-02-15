import pandas as pd
import numpy as np
import os

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
    h5_to_dict("data/TRAXLZU12903D05F94.h5")

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
