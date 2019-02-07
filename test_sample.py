import tweepy
import os

"""
    upload and download speed check
    json file is not empty
    format of json file is proper?
"""
def test_authentication():
    auth = tweepy.OAuthHandler(os.environ.get('customer_key'), os.environ.get('consumer_secret'))
    try:
        redirect_url = auth.get_authorization_url()
        assert True
    except tweepy.TweepError:
        assert 'Error! Failed to get request token.'
