import tweepy
import os

from dotenv import load_dotenv

load_dotenv()

# Authenticating twitter with credentials from env
auth = tweepy.OAuthHandler(os.environ.get('consumer_key'), os.environ.get('consumer_secret'))
auth.set_access_token(os.environ.get('access_token'), os.environ.get('access_token_secret'))
api = tweepy.API(auth)

# Running speedtest-cli to get download and upload speed of the Internet
process =  os.popen("speedtest-cli  --simple")
preprocessed = process.read()
process.close()

ping, download, upload, _ = preprocessed.split('\n')

#Expected vs Actual Speed
message = "@Rogers, | Ignite 60 Plan | Actual Speed -  Download: {}, Upload: {}".format(download.split(':')[1], upload.split(':')[1])

#Posting message on twitter
api.update_status(message)
