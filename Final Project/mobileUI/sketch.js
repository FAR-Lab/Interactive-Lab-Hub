var mode = 0 //Home Screen
let bcFont

function preload(){
  bcFont = loadFont("Mattire.otf");
}

function setup() {
  createMetaTag();
  createCanvas(window.innerWidth, window.innerHeight, WEBGL);
}

function draw() {
  background(220);

  if (mode == 0) {
    home();
  } else if (mode == 1) {
    screen2();
  } else if (mode == 2) {
    screen3();
  }
  
}

function home() {
  textFont(bcFont, 20);
  textSize(width / 15);
  textAlign(CENTER, CENTER);
  background(255, 251, 232);
  let time = millis();
  rotateX(time / 1000);
  rotateZ(time / 1234);
  text('Afterlife Garden', 0, 0); 
  fill(0, 102, 153);
}

function createMetaTag() {
  let meta = createElement('meta');
  meta.attribute('name', 'viewport');
  meta.attribute('content', 'user-scalable=no,initial-scale=1,maximum-scale=1,minimum-scale=1,width=device-width,height=device-height');
  
  let head = select('head');
  meta.parent(head);
}