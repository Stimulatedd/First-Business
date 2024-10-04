# Import necessary libraries
import tweepy
from transformers import pipeline

# Twitter API credentials (Directly inserted, not recommended)
consumer_key = 'HnVwCsSovXltxFrmq6Y97aEyV'
consumer_secret = 'EAAJ07SHMouB7tpZoz290DjQsYGGOPTRST8g51Gtq8DX0HZZxu'
access_token = '1471604210806312960-3Agom13HSocwVTeX405f93R2Em2UeA'
access_token_secret = 'yTAtCLQi4WWszGL0EFb9KIhSOjp2MDJggJi3zrE4gK4IS'

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Function to generate a tweet using Hugging Face GPT-2
def generate_tweet(theme):
    generator = pipeline('text-generation', model='gpt2')
    result = generator(f'Tweet about {theme}', max_length=50, num_return_sequences=1, truncation=True)
    tweet = result[0]['generated_text'].strip()
    return tweet

# Generate and post the tweet
theme = "motivation"  # You can change the theme
tweet_content = generate_tweet(theme)
api.update_status(tweet_content)
print(f"Posted Tweet: {tweet_content}")

# Error handling for posting the tweet
try:
    api.update_status(tweet_content)
    print(f"Posted Tweet: {tweet_content}")
except tweepy.errors.Forbidden as e:
    print(f"Error: {e}")
    print("Check your permissions and ensure your app has write access.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
