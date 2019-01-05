# pyTweetRogerInternet
> Runs Intenet Speedtest, tweets the speed and tags rogers

# Travis CI Build status
[![Build Status](https://travis-ci.com/ardyflora/pytweetRogerInternet.svg?branch=master)](https://travis-ci.com/ardyflora/pytweetRogerInternet)

pyTweetRogerInternet is a bot that will periodically check the Internet speed, tweet a detailed message which will contain the Actual vs Expected speed. The tweet will also have Rogers tagged in the message, with some hashtags.

## Installation

OS X & Linux:

```sh
pip install tweepy
pip install python-dotenv
```

## Usage example

You can follow the documentation of tweepy, here:
http://docs.tweepy.org/en/3.7.0/getting_started.html#hello-tweepy

The code snippet from above:
```py
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
```

## Development setup
To install dependencies you can simply run "requirements.txt" file.
```sh
pip install -r /path/to/requirements.txt
```

## Release History
* 0.0.1
    * Work in progress

## Meta

Ripudaman Flora – [@RipudamanF](https://twitter.com/RipudamanF) – ripudamanflora@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/ardyflora/pytweetRogerInternet](https://github.com/ardyflora/)
