# client.py
# python 3.6
import random
import time
from paho.mqtt import client as mqtt_client
import os

broker = 'broker.emqx.io'
port = 1883
topic = "python/rev_model"
client_id = f'subscribe-{random.randint(0, 100)}'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

def on_disconnect(client, userdata, rc):
    print("Lost connection")

def on_message(client, userdata, msg):
    #sender_client_id = userdata.get(msg.topic, "Unknown")
    #print(f"Received message from client {msg.topic}: {msg.payload.decode()} ")
    #time.sleep(5)
    print(f"Received message from client {msg.topic} ... ")
    
    handle_rev(client, userdata, msg)

def handle_rev(client, userdata, msg):
    if msg.payload:
        print("File mymodel.pth đã được tạo và đang lưu...")
        payload_str = msg.payload  
        with open("mymodel.txt", "ab") as file:
            file.write(payload_str)
    else:    
        print("Payload rỗng. Không tạo được file.")
        client.on_disconnect()
   
def handle_train():
    if os.path.exists("mymodel.pt"):
        print("Tệp tin tồn tại.")
    else:
        print("Tệp tin không tồn tại.")


def run():
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect(broker, port)

    client.loop_start()
    
    # Subscribe to receive data from the specified topic
    client.subscribe(topic)

    while True:
        time.sleep(1)

if __name__ == '__main__':
    run()
