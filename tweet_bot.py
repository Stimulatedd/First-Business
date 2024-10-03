# Import necessary libraries
import tweepy
from transformers import pipeline

# Twitter API credentials
consumer_key = 'mdnWph0fdtygc2htNI74TWbgT'
consumer_secret = 'UNp4g71bOY7jT9CC6yVhqV9h9UiYsjuoIP9lWdpWLzIVasrUvw'
access_token = '1471604210806312960-IAWhWrJ5bmF7zjndFq0aXXYhdO2P4K'
access_token_secret = 'xJ3cGZySRtUZwwHL4B1z4OoowSMCPjWMcrxoX4QohAe3r'

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Function to generate a tweet using Hugging Face GPT-2
def generate_tweet(theme):
    generator = pipeline('text-generation', model='gpt2')
    result = generator(f'Tweet about {theme}', max_length=50, num_return_sequences=1)
    tweet = result[0]['generated_text'].strip()
    return tweet

# Generate and post the tweet
theme = "motivation"  # You can change the theme
tweet_content = generate_tweet(theme)
api.update_status(tweet_content)
print(f"Posted Tweet: {tweet_content}")
