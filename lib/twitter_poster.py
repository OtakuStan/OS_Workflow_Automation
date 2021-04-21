import tweepy
import os
from lib.creds import get_creds

def post_twitter(video_title,video_link):
    try:
        creds = get_creds()
        auth = tweepy.OAuthHandler(creds["CONSUMER_KEY"],creds["CONSUMER_SECRET"])
        auth.set_access_token(creds["ACCESS_TOKEN"],creds["ACCESS_TOKEN_SECRET"])
        api = tweepy.API(auth)
        tweet_content = f"This is a twitter Automation test. Otakustan has recently posted a New Video: \n {video_title}. Go check it out!!\n {video_link} \n #anime #anime2021"
        api.update_status(tweet_content) 
    except Exception as e:
        raise e
    # print(creds['CONSUMER_KEY'])