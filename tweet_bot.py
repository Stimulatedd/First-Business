# Import necessary libraries
import tweepy
from transformers import pipeline

# Twitter API credentials
bearer_token = 'AAAAAAAAAAAAAAAAAAAAALPdwAEAAAAAw8MtueNsnibVjiu3d5%2Bdj%2BAT48Y%3DSNxG6fITTyaoDVEnW1D5a3DNwNtpRHmGWFMXnCSPmhtmIWdocq'  # Use bearer token for v2 API

# Authenticate with Twitter
client = tweepy.Client(bearer_token=bearer_token)

# Function to generate a tweet using Hugging Face GPT-2
def generate_tweet(theme):
    generator = pipeline('text-generation', model='gpt2')
    result = generator(f'Tweet about {theme}', max_length=50, num_return_sequences=1)
    tweet = result[0]['generated_text'].strip()
    return tweet

# Generate and post the tweet
theme = "motivation"  # You can change the theme
tweet_content = generate_tweet(theme)

# Post the tweet using the v2 API
try:
    response = client.create_tweet(text=tweet_content)
    print(f"Posted Tweet: {tweet_content} with ID: {response.data['id']}")
except tweepy.TweepyException as e:
    print(f"Error posting tweet: {e}")
