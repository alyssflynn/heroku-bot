# Dependencies
import tweepy
import json
import time
from config import consumer_key, consumer_secret, access_token, access_token_secret

# # Twitter API Keys
# consumer_key = "VzVpUISHIoFO3ccROGFM8DDVp"
# consumer_secret = "0aKIzZ8TzfCQAYrexN3kGcWXKd9KdsOx1CLO0nckOneye7TLoj"
# access_token= "999444856920518658-YMkLLZwqGYPtLqPSxaWjbocbDLRSvSI"
# access_token_secret = "LUfm6I7sHwUrHXBMvFEazOXSS2imeasYI7pOgHvDW1j6w"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE