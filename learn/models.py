from torch import nn


class RecommendationModel(nn.Module):
    def __init__(self, num_songs, embedding_dim):
        super().__init__()
        self.embedding = nn.Embedding(num_songs, embedding_dim)
        self.fc1 = nn.Linear(embedding_dim, 12)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(12, 12)
        self.fc3 = nn.Linear(12, num_songs)

    def forward(self, x):
        x = self.embedding(x)
        # x = x.mean(dim=1)
        x = x.max(dim=1)[0]
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x
