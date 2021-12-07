import eventlet
import json
from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
import uuid
import certifi
import ssl
from time import strftime

eventlet.monkey_patch()

app = Flask(__name__)

#app.config['SECRET'] = 'my secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'farlab.infosci.cornell.edu'
app.config['MQTT_BROKER_PORT'] = 8883
app.config['MQTT_CLIENT_ID'] = 'flask_mqtt'
app.config['MQTT_USERNAME'] = 'idd'
app.config['MQTT_PASSWORD'] = 'device@theFarm'
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = True
app.config['MQTT_TLS_VERSION'] = ssl.PROTOCOL_TLS
app.config['MQTT_TLS_INSECURE'] = True
app.config['MQTT_TLS_CA_CERTS'] = certifi.where()


mqtt = Mqtt(app)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    print(data)
    mqtt.publish(data['topic'], data['message'])


@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'])

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    msg = message.payload.decode()
    if message.topic == 'IDD/syw/cap':
        if '0' in message.payload.decode('UTF-8'):
            msg = 'PATIENT SOS'
        elif '2' in message.payload.decode('UTF-8'):
            msg = 'Patient requests to be moved'
        elif '11' in message.payload.decode('UTF-8'):
            msg = 'Patient requests food'
        elif '4' in message.payload.decode('UTF-8'):
            msg = 'Patient has taken medication'
        elif '8' in message.payload.decode('UTF-8'):
            msg = 'Patient requests assistance with the bathroom'
        elif '5' in message.payload.decode('UTF-8'):
            msg = 'Patient requests water'
        elif '6' in message.payload.decode('UTF-8'):
            msg = 'Patient requests general assistance'
    elif message.topic == 'IDD/syw/multi-distance':
        if 'Out of bed' in message.payload.decode('UTF-8'):
            msg = 'Patient is out of bed'
        else:
            msg = 'Patient is in bed'
    data = dict(
        topic=message.topic,
        time = strftime("%a, %d %b %Y %H:%M:%S"),
        payload=msg
    )
    print(data['time'], data['topic'], data['payload'])
    socketio.emit('mqtt_message', data=data)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    mqtt.subscribe('IDD/syw/cap')
    mqtt.subscribe('IDD/syw/multi-distance')


@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)


if __name__ == '__main__':
    # important: Do not use reloader because this will create two Flask instances.
    # Flask-MQTT only supports running with one instance
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=False)
