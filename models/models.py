from torch import nn
from learn.preprocess import num_songs
from learn.process import embedding_dim, input_len

model = nn.Sequential(
    nn.Embedding(num_songs, embedding_dim),
    nn.Flatten(),
    nn.Linear(embedding_dim * input_len, 12),
    nn.ReLU(),
    nn.Linear(12, 12),
    nn.ReLU(),
    nn.Linear(12, num_songs),
)
