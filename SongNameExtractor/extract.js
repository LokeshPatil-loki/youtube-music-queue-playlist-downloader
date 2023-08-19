const queue = document.querySelectorAll("#contents.style-scope.ytmusic-player-queue")[1];
const queueItems = queue.querySelectorAll("ytmusic-player-queue-item");
const playlistName = "Queued Items"
const songNameList = []
Array.from(queueItems).forEach(item => {
    const title = item.querySelector(".song-title").innerText
    const by = item.querySelector(".byline").innerText
    const fullName = `${title} by ${by}`;
    songNameList.push(fullName);
});

const socket = new WebSocket("ws://localhost:6060");

socket.onmessage = ({data}) => {
    data = JSON.parse(data);
    const percentage = (data[1]/data[2]) * 100;
    console.log(data[0],`\nProgress ${percentage} %`);

};

socket.onopen = () => {
    console.log("connected to download server");
    socket.send(JSON.stringify(songNameList))
}
