import requests
import random
import webbrowser
from secretsUWU.env import API_KEY

def open_video(query):
    
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 10,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "items" not in data:
        print("this gosh darn video ain't working :P")
        return

    videos = data["items"][:5]
    video = random.choice(videos)

    video_id = video["id"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    webbrowser.open(video_url)