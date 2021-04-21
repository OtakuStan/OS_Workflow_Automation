from lib.twitter_poster import post_twitter
from lib.youtube import get_latest_video
import json
import datetime
import time
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from apscheduler.triggers.cron import CronTrigger

# video_title='Top 10 Wholesome anime for Christmas'
# video_link = 'https://youtu.be/hpqmFF1P-NA'

# post_twitter(video_title, video_link)
VERSION="0.0.1"
class Automate_Twitter():
    def __init__(self,version):
        self.version = version
        # self.scheduler = AsyncIOScheduler()

    def automating_twitter(self):
        print("Getting Tweet Data")
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
            post_twitter(new_title,url)
            print(new_title)
        else:
            print("No New Video")

    def run_automation(self):
        starttime = time.time()
        while True:
            print ("tick")
            self.automating_twitter()
            time.sleep(60.0 - ((time.time() - starttime) % 60.0))
        # self.scheduler.add_job(self.automating_twitter, CronTrigger(day_of_week=6, minute=1))


automate = Automate_Twitter(version=VERSION)
