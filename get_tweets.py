# Import the necessary libraries
import tweepy
import os

# Set up your API keys as environment variables
consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token,
                                access_token_secret)

# Create an API object
api = tweepy.API(auth)

# Get the tweets from the specified user
# Replace "user" with the actual Twitter username
tweets = api.user_timeline(screen_name="caesars", count=20)
for tweet in tweets:
  # print(dir(tweet))
  # print(dir(tweet))
  print(tweet.text)
  # print(tweet.source_url)
  print("https://twitter.com/twitter/statuses/" + str(tweet.id))
  print(" ")
