#Python Script to download Youtube Videos for educational purpose only

import yt_dlp

#read video URL

url = input("Enter Video URL : ")
ydl_opts={}

#download the video

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download Successfull")
