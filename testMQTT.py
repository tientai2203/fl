import paho.mqtt.client as mqtt
import time
import random

broker = 'broker.emqx.io'
port = 1883
topic = "python/rev_model"
client_id = f'subscribe-{random.randint(0, 100)}'


def on_connect(client, userdate, flags, rc):
    global loop_flag
    print("In on_connect callback")
    loop_flag = 0

client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker)
client.loop_start()

loop_flag = 1
counter = 0
while loop_flag ==1:
    print("watting for callbacl to occur ", counter)
    time.sleep(0.1)
    counter+=1
    
client.disconnect()
client.loop_stop()