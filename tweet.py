import tweepy

from miserable import generate
from secrets import app_key, app_secret, token_key, token_secret

auth = tweepy.OAuthHandler(app_key, app_secret)
auth.set_access_token(token_key, token_secret)
tweepy.API(auth).update_status(status=generate())
