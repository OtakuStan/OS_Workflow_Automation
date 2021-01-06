import tweepy
import os
from lib.creds import get_creds

def post_twitter(video_title,video_link):
    try:
        creds = get_creds()
        auth = tweepy.OAuthHandler(creds["CONSUMER_KEY"],creds["CONSUMER_SECRET"])
        auth.set_access_token(creds["ACCESS_TOKEN"],creds["ACCESS_TOKEN_SECRET"])
        api = tweepy.API(auth)
        tweet_content = "Otakustan has Posted a Video:" + " " + video_title + " " + video_link
        api.update_status(tweet_content) 
    except Exception as e:
        raise e
    # print(creds['CONSUMER_KEY'])