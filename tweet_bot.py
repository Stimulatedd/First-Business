import tweepy

# Your API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Try posting a simple tweet
try:
    api.update_status("Hello, Twitter!")
    print("Tweet posted successfully!")
except tweepy.TweepyException as e:
    print(f"Error posting tweet: {e}")
