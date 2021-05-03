import paho.mqtt.client as mqtt
import uuid

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

radio_text = """I have a slight fear we  got so excited about this season  that the next one we could get so  anticipatory fit and then were
going to get let down. For me, Im  sorry if you havent seen the last  episode because we are spoiling it  for you, but the last one was a bit  
of a damp squid. At least they  didnt go ridiculous, but I was  like, oh, is that it But the  problem is that we know that H and I is not great 
and we know that people allowed him to be  promoted to that level so we know  there are senior people. There were  too many obections to the idea of
systemic option for me. Follow the  money. Yeah, exactly."""

radio_list = radio_text.split()

while True:
  topic = f"IDD/mmmradio"
  for val in radio_list:
        client.publish(topic, val)
  
  

