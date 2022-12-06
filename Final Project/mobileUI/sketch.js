let mode;
let bcFont;
let data;
let smallPoint, largePoint;
let showText = true;
let i; //make image come out faster


function preload(){
  bcFont = loadFont("Mattire.otf");
  Hector = loadImage('Hector.png');
  Imelda = loadImage("Imelda.png");
  Julio = loadImage("Julio.png");
  Rosita = loadImage("Rosita.png");
  Victoria = loadImage("Victoria.png");
  data = loadJSON("data.json");

}

function setup() {
  createMetaTag();
  createCanvas(window.innerWidth, window.innerHeight);
  smallPoint = 4;
  largePoint = 10;
  Hector.loadPixels();
  Imelda.loadPixels();
  Julio.loadPixels();
  Rosita.loadPixels();
  Victoria.loadPixels();
  noStroke();
  background(255, 251, 232);
}

function startBackgound() {
  background(146, 115, 98)
}


function draw() {
  mode = data[0].layer;
  //translate(-width/2,-height/2,0);
  if (mode == 0) {
    home();
  } else if (mode == 1){
    hector();
  }
  else if (mode == 2) {
    victoria();
  }
  else if (mode == 3) {
    julio();
  }
  else if (mode == 4) {
    rosita();
}
  else if (mode == 5) {
    victoria();
}
}

//Home Screen
function home() {
  background(255, 251, 232);
  textFont(bcFont, 20);
  textSize(width / 10);
  textAlign(CENTER,CENTER);
  if (showText){
    text('Afterlife Garden', width/2,height/2);
    fill(51,45,33);
  }
}

// End of Home Screen

//Family Memeber 1: Hector
function hector() {
  //let pointillize = map(mouseX, 0, width, smallPoint, largePoint);
  for(i=0; i < 10; i++){
    let x = floor(random(Hector.width));
    let y = floor(random(Hector.height));
    let Hpix = Hector.get(x, y);
    fill(Hpix);
    ellipse(x, y, 5, 5);
  }
}

// End of Hector

//Family Memeber 2: Imelda
function imelda() {
  //let pointillize = map(mouseX, 0, width, smallPoint, largePoint);
  Imelda.resize(width, 0)
  for(i=0; i < 10; i++){
    let x = floor(random(Imelda.width));
    let y = floor(random(Imelda.height));
    let Ipix = Imelda.get(x, y);
    fill(Ipix);
    ellipse(x, y, 5, 5);
  }
}
// End of Imelda
  
//Family member3 Julio
function julio() {
  //let pointillize = map(mouseX, 0, width, smallPoint, largePoint);
  Julio.resize(width, 0)
  for(i=0; i < 10; i++){
    let x = floor(random(Julio.width));
    let y = floor(random(Julio.height));
    let Jpix = Julio.get(x, y);
    fill(Jpix);
    ellipse(x, y, 5, 5);
  }
}
//End of Julio

//Family member 4 Rosita
function rosita() {
  //let pointillize = map(mouseX, 0, width, smallPoint, largePoint);
  Rosita.resize(width, 0)
  for(i=0; i < 10; i++){
    let x = floor(random(Rosita.width));
    let y = floor(random(Rosita.height));
    let Rpix = Rosita.get(x, y);
    fill(Rpix);
    ellipse(x, y, 5, 5);
  }
}
//End of Rosita

//Family member 4 Rosita
function victoria() {
  //let pointillize = map(mouseX, 0, width, smallPoint, largePoint);
  Victoria.resize(width, 0)
  for(i=0; i < 10; i++){
    let x = floor(random(Victoria.width));
    let y = floor(random(Victoria.height));
    let Vpix = Victoria.get(x, y);
    fill(Vpix);
    ellipse(x, y, 5, 5);
  }
}
//End of Victoria

function createMetaTag() {
  let meta = createElement('meta');
  meta.attribute('name', 'viewport');
  meta.attribute('content', 'user-scalable=no,initial-scale=1,maximum-scale=1,minimum-scale=1,width=device-width,height=device-height');
  
  let head = select('head');
  meta.parent(head);
}


