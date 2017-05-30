import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("sensors/outside/garden")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload)[1:])
    jdata = json.loads(msg.payload.decode('utf-8'))
    print("Temp: " + str(jdata['T']))
    print("Humidity: " + str(jdata['H']))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)

client.loop_forever()
