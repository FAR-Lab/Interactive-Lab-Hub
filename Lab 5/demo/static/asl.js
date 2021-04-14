const socket = io();
socket.on('connect', () => {
});

const read_words = document.getElementById('read-words');

setInterval(() => {
  socket.emit('ping-gps', 'dat')
}, 300)

socket.on('disconnect', () => {
  console.log('disconnect')
  mic.src = ''

  });

socket.on('new_letter', data => {
    read_words.innerHTML = read_words.innerHTML + data.letter;
});