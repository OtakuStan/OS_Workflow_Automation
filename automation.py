from lib.twitter_poster import post_twitter
from lib.youtube import get_latest_video
import json
import datetime
import time

VERSION="0.0.1"
class Automate_Twitter():
    def __init__(self,version):
        self.version = version

    def automating_twitter(self):
        with open('data.json','r') as f:
            data=json.load(f)
            past_title = data["title"]

        new_title = get_latest_video()[0]
        url = get_latest_video()[1]
        if new_title is not None and url is not None:
          if past_title != new_title:
              data["title"]=new_title
              data["url"] = url
              data["last_updated"]=str(datetime.date.today())
              with open("data.json", "w") as f:
                  json.dump(data,f)
              post_twitter(new_title,url)
          else:
              print("No New Video")

    def run_automation(self):
        starttime = time.time()
        while True:
            print ("tick")
            self.automating_twitter()
            time.sleep(900.0 - ((time.time() - starttime) % 900.0))


automate = Automate_Twitter(version=VERSION)
