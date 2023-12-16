
#include <WiFi.h>
#include "SparkFunLSM6DS3.h"
#include "Wire.h"
#include "SPI.h"
#include <PubSubClient.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"
#include <WiFiClient.h>
#include <WiFiServer.h>
#include <WiFiUdp.h>
#include <WiFiClientSecure.h>
#include "Adafruit_DRV2605.h"


//Global Setting
int network_enable = 1;


//WIFI Config
//const char* ssid = "WhiteSky-Cornell";
//const char* password = "4xjf6grn";
const char* ssid = "Xiaomi 13 Ultra";
const char* password = "qwertyuiop";
//

//Sensor Config
LSM6DS3 myIMU(I2C_MODE, 0x6A);  //Default constructor is I2C, addr 0x6B
Adafruit_DRV2605 drv;
//

//MQTT Config
const char* mqtt_broker = "farlab.infosci.cornell.edu";
const int mqtt_port = 8883;
const char* mqtt_username = "idd";
const char* mqtt_password = "device@theFarm";
const char* topic = "IDD/Cube";
//openssl s_client -connect farlab.infosci.cornell.edu:8883 -showcerts
const char* ROOT_CERT = "-----BEGIN CERTIFICATE-----\n"
"MIID0zCCArugAwIBAgIQVmcdBOpPmUxvEIFHWdJ1lDANBgkqhkiG9w0BAQwFADB7\n"
"MQswCQYDVQQGEwJHQjEbMBkGA1UECAwSR3JlYXRlciBNYW5jaGVzdGVyMRAwDgYD\n"
"VQQHDAdTYWxmb3JkMRowGAYDVQQKDBFDb21vZG8gQ0EgTGltaXRlZDEhMB8GA1UE\n"
"AwwYQUFBIENlcnRpZmljYXRlIFNlcnZpY2VzMB4XDTE5MDMxMjAwMDAwMFoXDTI4\n"
"MTIzMTIzNTk1OVowgYgxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpOZXcgSmVyc2V5\n"
"MRQwEgYDVQQHEwtKZXJzZXkgQ2l0eTEeMBwGA1UEChMVVGhlIFVTRVJUUlVTVCBO\n"
"ZXR3b3JrMS4wLAYDVQQDEyVVU0VSVHJ1c3QgRUNDIENlcnRpZmljYXRpb24gQXV0\n"
"aG9yaXR5MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEGqxUWqn5aCPnetUkb1PGWthL\n"
"q8bVttHmc3Gu3ZzWDGH926CJA7gFFOxXzu5dP+Ihs8731Ip54KODfi2X0GHE8Znc\n"
"JZFjq38wo7Rw4sehM5zzvy5cU7Ffs30yf4o043l5o4HyMIHvMB8GA1UdIwQYMBaA\n"
"FKARCiM+lvEH7OKvKe+CpX/QMKS0MB0GA1UdDgQWBBQ64QmG1M8ZwpZ2dEl23OA1\n"
"xmNjmjAOBgNVHQ8BAf8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zARBgNVHSAECjAI\n"
"MAYGBFUdIAAwQwYDVR0fBDwwOjA4oDagNIYyaHR0cDovL2NybC5jb21vZG9jYS5j\n"
"b20vQUFBQ2VydGlmaWNhdGVTZXJ2aWNlcy5jcmwwNAYIKwYBBQUHAQEEKDAmMCQG\n"
"CCsGAQUFBzABhhhodHRwOi8vb2NzcC5jb21vZG9jYS5jb20wDQYJKoZIhvcNAQEM\n"
"BQADggEBABns652JLCALBIAdGN5CmXKZFjK9Dpx1WywV4ilAbe7/ctvbq5AfjJXy\n"
"ij0IckKJUAfiORVsAYfZFhr1wHUrxeZWEQff2Ji8fJ8ZOd+LygBkc7xGEJuTI42+\n"
"FsMuCIKchjN0djsoTI0DQoWz4rIjQtUfenVqGtF8qmchxDM6OW1TyaLtYiKou+JV\n"
"bJlsQ2uRl9EMC5MCHdK8aXdJ5htN978UeAOwproLtOGFfy/cQjutdAFI3tZs4RmY\n"
"CV4Ks2dH/hzg1cEo70qLRDEmBDeNiXQ2Lu+lIg+DdEmSx/cQwgwp+7e9un/jX9Wf\n"
"8qn0dNW44bOwgeThpWOjzOoEeJBuv/c=\n"
"-----END CERTIFICATE-----\n";

WiFiClientSecure espClient;
PubSubClient mqttClient(espClient);

int current_orientation;
int pre_1_orientation;
int pre_2_orientation;
int pre_3_orientation;
int current_rotation;
int flip, p1flip, p2flip;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000);  //relax...
  Serial.println("Processor came out of reset.\n");

  // Let's choose an unsupported setting...
  myIMU.settings.accelSampleRate = 404;  // Typo, 'meant' to type '104'

  // Make a SensorSettings object to remember what you wanted to set everyhting to
  SensorSettings settingsIWanted;

  //Call .begin() to configure the IMU - supplying pointer to the SensorSettings structure
  myIMU.begin(&settingsIWanted);

  // Compare the sensor settings structure to know if anything was changed
  compareSettings(settingsIWanted);

  if (! drv.begin()) {
    Serial.println("Could not find DRV2605");
    while (1) delay(10);
  }
  int count = 0;
  if(network_enable){
    WiFi.mode(WIFI_STA);  //Optional
    WiFi.begin(ssid, password);
    Serial.println("\nConnecting");
    while (WiFi.status() != WL_CONNECTED) {
      delay(1000);
      Serial.println("Connecting to WiFi...");
      count += 1;
      if (count > 10){
        haptic(12);
        haptic(12);
        haptic(12);
        haptic(12);
        haptic(12);
        Serial.println("\Failed to the WiFi network");
        network_enable = 0;
        break;
      }
    }
    Serial.println("\nConnected to the WiFi network");
    Serial.print("Local ESP32 IP: ");
    Serial.println(WiFi.localIP());
    espClient.setCACert(ROOT_CERT);
    haptic(70);
  }
  current_orientation = 0;
  pre_1_orientation = 0;
  pre_2_orientation = 0;
  pre_3_orientation = 0;
  flip = 0;
  p1flip = 0;
  p2flip = 0;
}


void loop() {
  //MQTT Connection
  if(network_enable){
  if (!mqttClient.connected()) {    
    mqttClient.setServer(mqtt_broker, mqtt_port);
    // set the callback function
    mqttClient.setCallback(callback);
    Serial.println("Connecting to MQTT Broker...");
    while (!mqttClient.connected()) {
      Serial.println("Reconnecting to MQTT Broker..");
      String clientId = "ESP32Client-";
      clientId += String(random(0xffff), HEX);
      if (mqttClient.connect(clientId.c_str(), mqtt_username, mqtt_password)) {
         Serial.println("Connected to MQTT BRoker!.");
         // subscribe to topic
         mqttClient.subscribe("IDD/Cube");
         mqttClient.publish("IDD/Cube", "testing hello");
         haptic(70);
      } else {
          Serial.print("failed with state ");
          Serial.print(mqttClient.state());
          haptic(12);
          haptic(12);
          haptic(12);
          delay(2000);
      }
     }
    }
    mqttClient.loop();
  }

  //

  //Seneor Read
  //Get all parameters
  //Serial.print("\nAccelerometer:\n");
  //Serial.print(" X ACC= ");
  //Serial.println(myIMU.readFloatAccelX(), 4);
  //Serial.print(" Y ACC= ");
  //Serial.println(myIMU.readFloatAccelY(), 4);
  //Serial.print(" Z ACC= ");
  //Serial.println(myIMU.readFloatAccelZ(), 4);
  //Serial.print("\nGyroscope:\n");
  //Serial.print(" X Gyro= ");
  //Serial.println(myIMU.readFloatGyroX(), 4);
  //Serial.print(" Y Gyro= ");
  //Serial.println(myIMU.readFloatGyroY(), 4);
  //Serial.print(" Z Gyro= ");
  //Serial.println(myIMU.readFloatGyroZ(), 4);
  float x_acc, y_acc, z_acc, x_gyro, y_gyro, z_gyro;
  x_acc = myIMU.readFloatAccelX();
  y_acc = myIMU.readFloatAccelY();
  z_acc = myIMU.readFloatAccelZ();
  x_gyro = myIMU.readFloatGyroX();
  y_gyro = myIMU.readFloatGyroY();
  z_gyro = myIMU.readFloatGyroZ();
  pre_3_orientation = pre_2_orientation;
  pre_2_orientation = pre_1_orientation;
  pre_1_orientation = current_orientation;
  current_orientation = orientation(x_acc, y_acc, z_acc);
  Serial.print("current_orientation");
  Serial.println(current_orientation);
  p2flip = p1flip;
  p1flip = flip;
  flip = flip_cmd(current_orientation,pre_1_orientation,pre_2_orientation);
  float totalAcceleration = abs(x_acc) + abs(y_acc) + abs(z_acc);
  float totalGyro= abs(x_gyro) + abs(y_gyro) + abs(z_gyro);
  float error_rotation_threshold = 10;
  float small_rotation_threshold = 100;
  float small_rotation_threshold_cap = 500;
  get_instruction(flip);
  float large_rotation_threshold = 800;
  float shake_threshold = 1.7;
  //stable
  Serial.println(flip);
  
  if (totalAcceleration > shake_threshold) {
    // Shaking detected, you can take action here
    Serial.println("Shaking!");
    mqttClient.publish("IDD/Cube", "11");
    haptic(47);
  }else if(flip == 20){
    current_rotation = rotation(x_gyro, y_gyro, z_gyro);
    get_ori_instruction(current_rotation);
  }
  /*
  if (totalAcceleration > shake_threshold) {
    // Shaking detected, you can take action here
    Serial.println("Shaking!");
    haptic(47);
  }else{
    if (totalGyro < error_rotation_threshold){
    }
    else if (totalGyro > large_rotation_threshold) {
      // Shaking detected, you can take action here
      Serial.println("Large Rotation Detected!");
    }else if (totalGyro > small_rotation_threshold){
      Serial.println("Small Rotation Detected!");
    }
  }
  */

  delay(500);
}

int flip_cmd(int c_o, int p_1_o, int p_2_o){
  if (c_o == 1 &&  p_1_o != 1 && p_2_o != 1 && p_2_o != -1){
    Serial.println("flip to +x");
    if (p_1_o == 2 or p_2_o == 2){
      Serial.println("to right wave");
      return 3;
    }
    return 5;
  }else if (c_o == 2 && p_1_o != 2 && p_2_o != 2 && p_2_o != -1){
    Serial.println("flip to +y");
    if (p_1_o == 1 or p_2_o == 1){
      Serial.println("to left wave");
      return 4;
    }else if (p_1_o == 4 or p_2_o == 4){
      Serial.println("to right wave");
      return 3;
    }else if (p_1_o == 6 or p_2_o == 6){
      Serial.println("to dwon wave");
      return 1;
    }else if (p_1_o == 3 or p_2_o == 3){
      Serial.println("to top wave");
      return 2;
    }
    return 10;
  }else if (c_o == 3 && p_1_o != 3 && p_2_o != 3 && p_2_o != -1){
    Serial.println("flip to +z");
    if (p_1_o == 2 or p_2_o == 2){
      Serial.println("to down wave");
      return 1;
    }
    return 6;
  }else if (c_o == 4 &&  p_1_o != 4 && p_2_o != 4 && p_2_o != -1){
    Serial.println("flip to -x");
    if (p_1_o == 2 or p_2_o == 2){
      Serial.println("to left wave");
      return 4;
    }
    return 7;
  }else if (c_o == 5 && p_1_o != 5 && p_2_o != 5 && p_2_o != -1){
    Serial.println("flip to -y");
    if (p_1_o == 2 or p_2_o == 2){
      Serial.println("down side to up side");
      return 99;
    }
    return 10;
  }else if (c_o == 6 && p_1_o != 6 && p_2_o != 6 && p_2_o != -1){
    Serial.println("flip to -z");
    if (p_1_o == 2 or p_2_o == 2){
      Serial.println("to top wave");
      return 2;
    }
    return 8;
  }else if (c_o == p_1_o && p_1_o == p_2_o){
    return 20;
  }else{
    return -1;
  }
}

int orientation(float x, float y, float z){
  if ((x)>0.95 && (x)<1.05 && ((abs(y)+abs(z)) < 0.2)){
    return 1;
  }else if((y)>0.95 && (y)<1.05 && ((abs(x)+abs(z)) < 0.2)){
    return 2;
  }else if((z)>0.95 && (z)<1.05 && ((abs(x)+abs(y)) < 0.2)){
    return 3;
  }else if (-(x)>0.95 && -(x)<1.05 && ((abs(y)+abs(z)) < 0.2)){
    return 4;
  }else if(-(y)>0.95 && -(y)<1.05 && ((abs(x)+abs(z)) < 0.2)){
    return 5;
  }else if(-(z)>0.95 && -(z)<1.05 && ((abs(x)+abs(y)) < 0.2)){
    return 6;
  }else{
    return -1;
  } 
}

int rotation(float x, float y, float z){
  int th = 50;
  int th_cap = 150;
  int error_max =30;
  if ((x)> th && (x)< th_cap && ((abs(y)+abs(z)) < error_max)){
    Serial.println("x_pos_r");
    return 1;
  }else if (-(x)> th && -(x)< th_cap && ((abs(y)+abs(z)) < error_max)){
    Serial.println("x_neg_r");
    return 2;
  }else if((y)> th && (y)< th_cap && ((abs(x)+abs(z)) < error_max)){
    Serial.println("y_pos_r");
    return 3;
  }else if(-(y)> th && -(y)< th_cap && ((abs(x)+abs(z)) < error_max)){
    Serial.println("y_neg_r");
    return 4;
  }else if((z)> th && (z)< th_cap && ((abs(x)+abs(y)) < error_max)){
    Serial.println("z_pos_r");
    return 5;
  }else if(-(z)> th && -(z)< th_cap && ((abs(x)+abs(y)) < error_max)){
    Serial.println("z_neg_r");
    return 6;
  }else{
    return -1;
  } 
}

void get_instruction(int code){
  if (code == 1){
    mqttClient.publish("IDD/Cube", "1");
    haptic(70);
  }else if (code == 2){
    mqttClient.publish("IDD/Cube", "2");
    haptic(70);
  }else if (code == 3){
    mqttClient.publish("IDD/Cube", "3");
    haptic(70);
  }else if (code == 4){
    mqttClient.publish("IDD/Cube", "4");
    haptic(70);
  }else if (code == 5){
    mqttClient.publish("IDD/Cube", "5");
    haptic(70);
  }else if (code == 6){
    mqttClient.publish("IDD/Cube", "6");
    haptic(47);
  }else if (code == 7){
    mqttClient.publish("IDD/Cube", "7");
    haptic(47);
  }else if (code == 8){
    mqttClient.publish("IDD/Cube", "8");
    haptic(47);
  }else if (code == 9){
    mqttClient.publish("IDD/Cube", "9");
    haptic(14);
  }else if (code == 10){
    mqttClient.publish("IDD/Cube", "10");
    haptic(14);
  }else if (code == 99){
    mqttClient.publish("IDD/Cube", "99");
    haptic(66);
  }
}

void get_ori_instruction(int code){
  if (code == 1){
    mqttClient.publish("IDD/Cube", "12");
    haptic(12);
  }else if (code == 2){
    mqttClient.publish("IDD/Cube", "13");
    haptic(12);
  }else if (code == 3){
    mqttClient.publish("IDD/Cube", "14");
    haptic(12);
  }else if (code == 4){
    mqttClient.publish("IDD/Cube", "15");
    haptic(12);
  }else if (code == 5){
    mqttClient.publish("IDD/Cube", "16");
    haptic(12);
  }else if (code == 6){
    mqttClient.publish("IDD/Cube", "17");
    haptic(12);
  }
}


void mqtt_cmd(char* cmd){
  Serial.println(cmd);
  //mqttClient.publish("IDD/Cube", cmd);
}

void haptic(int effect){
  drv.setWaveform(0, effect);  // play effect 
  drv.setWaveform(1, 0);       // end waveform

  // play the effect!
  drv.go();
}

void compareSettings(SensorSettings desiredSettings) {
  if (myIMU.settings.accelBandWidth != desiredSettings.accelBandWidth) { Serial.println("'accelBandWidth' was changed!"); }
  if (myIMU.settings.accelRange != desiredSettings.accelRange) { Serial.println("'accelRange' was changed!"); }
  if (myIMU.settings.accelSampleRate != desiredSettings.accelSampleRate) { Serial.println("'accelSampleRate' was changed!"); }
  if (myIMU.settings.gyroRange != desiredSettings.gyroRange) { Serial.println("'gyroRange' was changed!"); }
  if (myIMU.settings.gyroSampleRate != desiredSettings.gyroSampleRate) { Serial.println("'gyroSampleRate' was changed!"); }
  // That's all the settings that might get changed in 'begin()'
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Callback - ");
  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
}