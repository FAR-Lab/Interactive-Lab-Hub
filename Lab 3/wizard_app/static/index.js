const socket = io();
socket.on('connect', () => {
});

const mic = document.getElementById('mic');
const play = document.getElementById('play');
const wordsIn = document.getElementById('wordsIn');
const send = document.getElementById('send');
const start = document.getElementById('start-game');
const detonate = document.getElementById('detonate');
const accept_color = document.getElementById('accept-color');
const reject_color = document.getElementById('reject-color');
const accept_name = document.getElementById('accept-name');
const reject_name = document.getElementById('reject-name');
const accept_riddle1 = document.getElementById('accept-riddle1');
const reject_riddle1 = document.getElementById('reject-riddle1');
const accept_riddle2 = document.getElementById('accept-riddle2');
const reject_riddle2 = document.getElementById('reject-riddle2');
const accept_riddle3 = document.getElementById('accept-riddle3');
const reject_riddle3 = document.getElementById('reject-riddle3');

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

detonate.onclick = () => {
    socket.emit('detonate')
}

accept_color.onclick = () => {
   socket.emit('color', 'accept')
}

reject_color.onclick =() => {
   socket.emit('color', 'reject')
}

accept_riddle1.onclick = () => {
   socket.emit('riddle1', 'accept')
}

reject_riddle1.onclick =() => {
   socket.emit('riddle1', 'reject')
}

accept_riddle2.onclick = () => {
   socket.emit('riddle2', 'accept')
}

reject_riddle2.onclick =() => {
   socket.emit('riddle2', 'reject')
}

accept_riddle3.onclick = () => {
   socket.emit('riddle3', 'accept')
}

reject_riddle3.onclick =() => {
   socket.emit('riddle3', 'reject')
}

