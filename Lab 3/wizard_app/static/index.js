const socket = io();
socket.on('connect', () => {
});

const mic = document.getElementById('mic');
const play = document.getElementById('play');
const wordsIn = document.getElementById('wordsIn');
const send = document.getElementById('send');
const accept_name = document.getElementById('accept-name');
const start = document.getElementById('start-game');

const src = mic.src
mic.src = ''

play.onclick = () => {
  if(mic.paused) {
  console.log('redo audio')
  mic.src = src
  mic.play()
  play.innerText='Pause'
  } else {
    mic.pause()
      mic.src = '';
    play.innerText='Eavesdrop'
  }
  
}

send.onclick = () => {
  socket.emit('speak', wordsIn.value)
  wordsIn.value = ''
}
wordsIn.onkeyup = (e) => { if (e.keyCode === 13) { send.click(); } };
  
setInterval(() => {
  socket.emit('ping-gps', 'dat')
}, 100)

socket.on('disconnect', () => {
  console.log('disconnect')
  mic.src = ''

  });

accept_name.onclick = () => {
   socket.emit('name', 'accept')
}

reject_name.onclick =() => {
   socket.emit('name', 'reject')
}

start.onclick = () => {
    socket.emit('start')
}
