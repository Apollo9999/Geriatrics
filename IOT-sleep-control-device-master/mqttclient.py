import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code" + str(rc))
    client.subscribe("Anan/one")
    client.subscribe("Anan/two")
    
def on_message(client, userdata, msg):
    print(msg.topic+ " " + str(msg.payload))
    if msg.payload == "Hello":
        print("msg 1 recd")
    if msg.payload == "World!":
        print("msg 2")


client= mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1833 , 60)
client.loop_forever()
