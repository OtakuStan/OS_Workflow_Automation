from lib.creds import get_creds
import requests

creds = get_creds()
api_key = creds["YOUTUBE_API_KEY"]
yt_channel_id = "UCcvnNBCZplzRkGCFyzNcwzg"
yt_base_url = "https://www.youtube.com/watch?v="

def get_latest_video() -> tuple:
  title = None
  url = None
  try:
    latest_video = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={yt_channel_id}&part=snippet,id&order=date&maxResults=1"
    recv=requests.get(latest_video)
    if "items" in recv.json():
      js = recv.json()["items"][0]

      title = js["snippet"]["title"]
      url = yt_base_url + js["id"]["videoId"]
      return (title,url)
    else:
      return (title,url)
  except Exception as e:
    raise e