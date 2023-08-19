import asyncio
import websockets
import json
from YoutbeMusicDownloader import getUrl, download_audio


async def onMessage(websocket):
    data = await websocket.recv()
    songsList = json.loads(data)
    urlList = []
    for idx,title in enumerate(songsList):
        url = getUrl(title)
        # urlList.append(url)
        print("{} -> {}".format(title,url))
        download_audio(url)
        await websocket.send(json.dumps([f"Downloaded {title}",idx+1,len(songsList)]))
    

async def main():
    async with websockets.serve(onMessage,"localhost",6060):
        print("Started Download Server")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

