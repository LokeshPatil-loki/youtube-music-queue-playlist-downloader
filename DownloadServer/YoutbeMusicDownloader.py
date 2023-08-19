from youtubesearchpython import VideosSearch
import subprocess
import json

def getUrl(title):
    videosSearch = VideosSearch(title, limit = 1)
    result = videosSearch.result()
    return result["result"][0]["link"]


def download_audio(url):
    command = ["yt-dlp","-f","ba","-x","--audio-format","mp3",url]

    process = subprocess.Popen(command,cwd="Downloads", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # print("Output:", output.decode('utf-8'))
    if error.decode('utf-8'):
        print("Error:", error.decode('utf-8'))

    print("Done")



# songsList = json.load(open("songs.json","rb"))
# urlList = []
# for title in songsList:
#     url = getUrl(title)
#     # urlList.append(url)
#     print("{} -> {}".format(title,url))
#     download_audio(url)


    

# 

# print()
