const control = document.getElementById('control');
const light = document.getElementById('light');
const play = document.getElementById('play');
const pause = document.getElementById('pause');
const audioIn = document.getElementById('audioIn');
const alarm1 = document.getElementById('alarm1');
const alarm2 = document.getElementById('alarm2');
const alarm3 = document.getElementById('alarm3');
const timers = document.getElementsByClassName('timer');
const audio = new Audio();
const clockTime = document.getElementById('clockTime');
let pickr;

const socket = io();

socket.on('connect', () => {
  socket.on('hex', (val) => {document.body.style.backgroundColor = val})
  socket.on('audio', (val) => {getSound(encodeURI(val));})
  socket.on('pauseAudio', (val) => {audio.pause();})
  socket.onAny((event, ...args) => {
  console.log(event, args);
});
socket.on('clockTime', (data) => {
  document.getElementById('clockTime').innerHTML = data.description;
});
});

//Couldn't seem to get this working
socket.on('clockTime', function(data) {
  document.getElementById('clockTime').innerHTML = data.description;
});

// enter controller mode
/* control.onclick = () => {
  console.log('control')
  // make sure you're not in fullscreen
  if (document.fullscreenElement) {
    document.exitFullscreen()
      .then(() => console.log('exited full screen mode'))
      .catch((err) => console.error(err));
  }
  // make buttons and controls visible
  document.getElementById('user').classList.remove('fadeOut');
  document.getElementById('controlPanel').style.opacity = 0.6;
  if (!pickr) {
    // create our color picker. You can change the swatches that appear at the bottom
    pickr = Pickr.create({
      el: '.pickr',
      theme: 'classic',
      showAlways: true,
      swatches: [
        'rgba(255, 255, 255, 1)',
        'rgba(244, 67, 54, 1)',
        'rgba(76, 175, 80, 1)',
        'rgba(255, 235, 59, 1)',
        'rgba(255, 140, 0, 1)',
        'rgba(0, 0, 0, 1)'
      ],
      components: {
        preview: false,
        opacity: false,
        hue: true,
      },
    });

    pickr.on('change', (e) => {
      // when pickr color value is changed change background and send message on ws to change background
      const hexCode = e.toHEXA().toString();
      document.body.style.backgroundColor = hexCode;
      socket.emit('hex', hexCode)
    });
  }
}; */

// Range taken from: https://stackoverflow.com/questions/29890093/how-can-i-generate-n-amount-of-colors-within-a-range-of-two-given-colors
var dynamicColorChange = function (start_r, start_g, start_b, end_r, end_g, end_b, waitVal) {
  var si = setInterval(function() {
          if (start_r < end_r) {
              start_r += 5;
          }else if(start_r > end_r){
          start_r -= 5;
          }
          if (start_g < end_g) {
              start_g += 5;
          }else if(start_g > end_g){
              start_g -= 5;
          }
          if (start_b < end_b) {
              start_b += 5;
          }else if(start_b > end_b){
              start_b -= 5;
          }
          document.body.style.backgroundColor = 'rgb(' + start_r + ',' + start_g + ',' + start_b + ')';
          socket.emit('hex', 'rgb(' + start_r + ',' + start_g + ',' + start_b + ')')
          if (start_r == end_r && start_g == end_g && start_b == end_b) {
              clearInterval(si);
          }
      }, waitVal);
};

light.onclick = () => {
  // safari requires playing on input before allowing audio
  audio.muted = true;
  audio.play().then(audio.muted=false)

  // in light mode make it full screen and fade buttons
  document.documentElement.requestFullscreen();
  document.getElementById('user').classList.add('fadeOut');
  // if you were previously in control mode remove color picker and hide controls
  if (pickr) {
    // this is annoying because of the pickr package
    pickr.destroyAndRemove();
    document.getElementById('controlPanel').append(Object.assign(document.createElement('div'), { className: 'pickr' }));
    pickr = undefined;
  }
  light.destroyAndRemove();
  alarm.destroyAndRemove();
  document.getElementById('controlPanel').style.opacity = 0;
};

for(var i = 0; i < timers.length; i++) {
  var timer = timers[i];
  timer.onclick = () => {
    dynamicColorChange(75, 175, 80, 30, 45, 55, 50);
    document.getElementById('clockTime').innerHTML = "2h 0m";
    socket.emit('clock');
  }
}

alarm1.onclick = () => {
  var waitTime = 50;
    // yellow
    var i = 0;
    var yellow = setInterval(function() {
      dynamicColorChange(255, 255, 55, 30, 45, 55, waitTime);
      i++; 
      if (i == 3) {
        clearInterval(yellow);
      }
    }, 3000);
  };

  alarm2.onclick = () => {
    var waitTime = 50;
    //orange
    var j = 0;
    var orange = setInterval(function() {
      dynamicColorChange(255, 140, 0, 30, 45, 55, waitTime);
      j++; 
      if (j == 3) {
        clearInterval(orange);
      }
    }, 3000);
  };

  alarm3.onclick = () => {
    var waitTime = 50;
  //red
  var k = 0;
  var red = setInterval(function() {
      socket.emit('shake'); 
      dynamicColorChange(245, 70, 55, 30, 45, 55, waitTime);
      k++;
      if (k == 3) {
        clearInterval(red);
      } 
    }, 3000);
};


const getSound = (query, loop = false, random = false) => {
  const url = `https://freesound.org/apiv2/search/text/?query=${query}+"&fields=name,previews&token=U5slaNIqr6ofmMMG2rbwJ19mInmhvCJIryn2JX89&format=json`;
  fetch(url)
    .then((response) => response.clone().text())
    .then((data) => {
      console.log(data);
      data = JSON.parse(data);
      if (data.results.length >= 1) var src = random ? choice(data.results).previews['preview-hq-mp3'] : data.results[0].previews['preview-hq-mp3'];
      audio.src = src;
      audio.play();
      console.log(src);
		  })
    .catch((error) => console.log(error));
};

play.onclick = () => {
  socket.emit('audio', audioIn.value)
  getSound(encodeURI(audioIn.value));
};
pause.onclick = () => {
  socket.emit('pauseAudio', audioIn.value)
  audio.pause();
};
audioIn.onkeyup = (e) => { if (e.keyCode === 13) { play.click(); } };
