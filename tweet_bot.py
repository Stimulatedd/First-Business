import tweepy
from transformers import pipeline

# Twitter API credentials
consumer_key = 'GHdNOl1bBFV6Tlq65xdKs5c4H'  # Replace with your actual consumer key
consumer_secret = 'JUSi3qDoMbVclLaCYN4MwHIFhdCaloAeGZGLPyMNJZ6NwD6Djn'  # Replace with your actual consumer secret
access_token = '1471604210806312960-0UjgJAvB7yl1QKsSA3RssAOmDHPrEU'  # Replace with your actual access token
access_token_secret = 'ZhUcMB9Bze6f51BeA88VdqeauPCWU8EZzPKKafhIIpAZn'  # Replace with your actual access token secret

import tweepy
# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Function to generate a tweet using Hugging Face GPT-2
def generate_tweet(theme):
    generator = pipeline('text-generation', model='gpt2')
    result = generator(f'Tweet about {theme}', max_length=50, truncation=True, num_return_sequences=1)
    tweet = result[0]['generated_text'].strip()
    return tweet

# Generate and post the tweet
theme = "motivation"  # You can change the theme
tweet_content = generate_tweet(theme)

# Post the tweet
try:
    api.update_status(tweet_content)
    print(f"Posted Tweet: {tweet_content}")
except tweepy.TweepyException as e:
    print(f"Error posting tweet: {e}")  # Updated to print the error message directly
