import requests
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/5.1.2_3/bin/ffmpeg"
from moviepy.editor import VideoFileClip, AudioFileClip
video_url = "https://149vod-adaptive.akamaized.net/exp=1674655904~acl=%2F6b903ae8-efb5-41fe-9f3d-1e1c7b42e494%2F%2A~hmac=c03ef1cb4f53bff146d0939a28748dbc4f5779aa5032036b2ce5fb0b3b2c0b99/6b903ae8-efb5-41fe-9f3d-1e1c7b42e494/parcel/video/741a4ea9.mp4"
audio_url = "https://149vod-adaptive.akamaized.net/exp=1674656360~acl=%2F6b903ae8-efb5-41fe-9f3d-1e1c7b42e494%2F%2A~hmac=0280910b878cd5adc3cca2277133810ed7822c2e1b6b2ea774cf89b048ce5d72/6b903ae8-efb5-41fe-9f3d-1e1c7b42e494/parcel/audio/b3cfc298.mp4"

video_data = requests.get(video_url).content
audio_data = requests.get(audio_url).content

with open("video.mp4", "wb") as video_file:
    video_file.write(video_data)

with open("audio.mp3", "wb") as audio_file:
    audio_file.write(audio_data)

video = VideoFileClip("video.mp4")
audio = AudioFileClip("audio.mp3")

final_video = video.set_audio(audio)
final_video.write_videofile("final_video.mp4")