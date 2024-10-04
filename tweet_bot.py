# Import necessary libraries 
import tweepy
from transformers import pipeline

# Twitter API credentials
consumer_key = 'GHdNOl1bBFV6Tlq65xdKs5c4H'  # Replace with your actual consumer key
consumer_secret = 'JUSi3qDoMbVclLaCYN4MwHIFhdCaloAeGZGLPyMNJZ6NwD6Djn'  # Replace with your actual consumer secret
access_token = '1471604210806312960-0UjgJAvB7yl1QKsSA3RssAOmDHPrEU'  # Replace with your actual access token
access_token_secret = 'ZhUcMB9Bze6f51BeA88VdqeauPCWU8EZzPKKafhIIpAZn'  # Replace with your actual access token secret

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

# Print the generated tweet for debugging
print(f"Generated Tweet: {tweet_content}")

# Check tweet length and post the tweet
if len(tweet_content) <= 280:
    try:
        api.update_status(tweet_content)
        print(f"Posted Tweet: {tweet_content}")
    except tweepy.TweepyException as e:
        # Print the error response and error code
        print(f"Error posting tweet: {e.response.text}")  # Prints the error response text
        print(f"Error Code: {e.api_code}")  # Prints the specific API error code
else:
    print("Tweet is too long!")
