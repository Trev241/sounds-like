from torch import nn


class SongEmbeddingModel(nn.Module):
    def __init__(self, embedding_dim, num_embeddings, input_len, target):
        super().__init__()
        self.flatten = nn.Flatten()
        self.embedding = nn.Embedding(num_embeddings, embedding_dim)
        self.fc = nn.Linear(embedding_dim * input_len, 256)
        self.relu = nn.ReLU()
        self.linear_1 = nn.Linear(256, 256)
        self.linear_2 = nn.Linear(256, num_embeddings)
        self.loss = nn.CrossEntropyLoss()
        self.target = target

    def forward(self, x):
        x = self.embedding(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        x = self.relu(x)
        x = self.linear_1(x)
        x = self.relu(x)
        x = self.linear_2(x)

        output = self.loss(x, self.target)
        output.backward()

        return x
