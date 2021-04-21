from lib.twitter_poster import post_twitter
from lib.youtube import get_latest_video
import json
import datetime

# video_title='Top 10 Wholesome anime for Christmas'
# video_link = 'https://youtu.be/hpqmFF1P-NA'

# post_twitter(video_title, video_link)

def automate_twitter():
    with open('data.json','r') as f:
        data=json.load(f)
        past_title = data["title"]

    new_title = get_latest_video()[0]
    url = get_latest_video()[1]
    if past_title != new_title:
        data["title"]=new_title
        data["url"] = url
        data["last_updated"]=str(datetime.date.today())
        with open("data.json", "w") as f:
            json.dump(data,f)
        print(new_title)

automate_twitter()
print("Tweet Send")