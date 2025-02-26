# Run the entire workflow as a consolidated process in Python
import learn.fetch as _
import torch

from learn.process import model
from learn.preprocess import unique, song_metadata

print(model)

# Make a prediction with the model
# Example: predictions = model(torch.tensor([65, 34, 12, 29]))

# Enter 4 songs as input. They must be encoded between 0 and num_songs - 1
profile = [12, 13, 14, 15]
logits = model(torch.tensor([profile]))
probabilities = torch.sigmoid(
    logits
)  # You must use sigmoid for mutli-label classification problems
# probabilities = F.softmax(logits, dim=1)        # You must use softmax for single label classification problems

# Returns the top 5 songs that the user is likely to interact with.
top_probs = torch.topk(probabilities, 10)

profile_ids = list(map(lambda idx: unique[idx], profile))
profile_titles = song_metadata.loc[song_metadata["song_id"].isin(profile_ids)]

rec_ids = list(map(lambda idx: unique[idx], top_probs.indices.squeeze_().tolist()))
rec_titles = song_metadata.loc[song_metadata["song_id"].isin(rec_ids)]

print(top_probs)
print(profile_titles[["title", "artist_name"]])
print(rec_titles[["title", "artist_name"]])
