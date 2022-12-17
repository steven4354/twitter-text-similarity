import requests
import os
import numpy as np
from scipy.spatial.distance import cosine

# https://huggingface.co/blog/getting-started-with-embeddings
model_id = "sentence-transformers/all-MiniLM-L6-v2"
hf_token = os.environ["HUGGING_FACE"]

api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}


def query(texts):
  response = requests.post(api_url,
                           headers=headers,
                           json={
                             "inputs": texts,
                             "options": {
                               "wait_for_model": True
                             }
                           })
  return response.json()


texts = [
  "How do I get a replacement Medicare card?",
  "What is the monthly premium for Medicare Part B?",
  "How do I terminate my Medicare Part B (medical insurance)?",
  "How do I sign up for Medicare?",
  "Can I sign up for Medicare Part B if I am working and have health insurance through an employer?",
  "How do I sign up for Medicare Part B if I already have Part A?",
  "What are Medicare late enrollment penalties?",
  "What is Medicare and who can get it?",
  "How can I get help with my Medicare Part A and Part B premiums?",
  "What are the different parts of Medicare?",
  "Will my Medicare premiums be higher because of my higher income?",
  "What is TRICARE ?",
  "Should I sign up for Medicare Part B if I have Veterans' Benefits?"
]

# Query the API to get the embeddings for each tweet
output = query(texts)

# Calculate the cosine similarity between each pair of tweets

num_tweets = len(texts)
similarity_matrix = np.zeros((num_tweets, num_tweets))
# for i in range(num_tweets):
#   for j in range(num_tweets):
#     if i == j:
#       # Skip the diagonal, as the cosine similarity of a tweet with itself is 0
#       continue
#     similarity_matrix[i, j] = 1 - cosine(output[i], output[j])

# # Find the two tweets with the highest cosine similarity
# most_similar_indices = np.argpartition(similarity_matrix, -2)[-2:]
# most_similar_tweets = [texts[i] for i in most_similar_indices]

# print("The two most similar tweets are:")
# for tweet in most_similar_tweets:
#   print(tweet)

most_similar_indices = np.argpartition(similarity_matrix, -2)[-2:]
most_similar_tweet_indices = [most_similar_indices[i].item() for i in range(len(most_similar_indices))]
most_similar_tweets = [texts[i] for i in most_similar_tweet_indices]
