import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

auth = tweepy.OAuthHandler(os.environ.get('customer_key'), os.environ.get('consumer_secret'))
auth.set_access_token(os.environ.get('access_token'), os.environ.get('access_token_secret'))

api = tweepy.API(auth)
api.update_status('Testing via script :: Using dotenv #python #tweepy #letlearningbegin')

# Get all the tweets
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)
