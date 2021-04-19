const socket = io();
socket.on('connect', () => {
});

const read_words = document.getElementById('read-words');
const video = document.getElementById('video-holder');
const checkin = document.getElementById('check-in');

checkin.onclick = () => {
  socket.emit('check_state')
};

setInterval(() => {
  socket.emit('ping-gps', 'dat')
  socket.emit('ping-video')
}, 4000);

socket.on('disconnect', () => {
  console.log('disconnect')
  mic.src = ''

  });

socket.on('new_letter', data => {
    read_words.innerHTML = data.letter + " Detected";
});

socket.on('new_frame', data => {
    video.src = video.src + "?time=" + Math.random().toString();
});
