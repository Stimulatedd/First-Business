import tweepy

# Your API credentials
consumer_key = 'Le8ncsi5FS7MFOuZN0l7WEiOf'
consumer_secret = 'chlQbS0221qf0WX4LWheZT7fVuUtmzn87UMjis8WZ4hDCgskKl'
access_token = '1471604210806312960-EDexpTgBqHbyuudLDCnpwavZy79t4Y'
access_token_secret = 'n2X4RPKJM6Wq78z8cl8hN5kXJ4wo9RozhvNx837JdTjCB'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Try posting a simple tweet
try:
    api.update_status("Hello, Twitter!")
    print("Tweet posted successfully!")
except tweepy.TweepyException as e:
    print(f"Error posting tweet: {e}")
