# server.py
import random
import time
from paho.mqtt import client as mqtt_server

broker = 'broker.emqx.io'
port = 1883
topic = "python/rev_model"

client_id = f'publish-{random.randint(0, 1000)}'

#file_path = "D:\WorkSpace\Test_DFL\FashionMnist_Dataset\FashionMnist.pt"
file_path = "D:\WorkSpace\Test_DFL\MQTT.txt"
#file_path = "D:\WorkSpace\Test_DFL\FashionMnist.pt"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}")

    client = mqtt_server.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    #test_handle(client)
    handle_msg_publish(client)

def handle_msg_publish(client):
    while True:
        with open(file_path, 'rb') as file:
            file_content = file.read()  # Đọc 1024 byte mỗi lần
            while file_content:
                time.sleep(1)
                # Gửi từng phần dữ liệu lên topic là tên file
                result = client.publish(topic, file_content)
                file_content = file.read()
                # result: [0, 1]
                status = result[0]
                if status == 0:
                    print(f"Sending to topic `{topic}`...")
                else:
                    print(f"Failed to send message to topic {topic}")
        print("All published")
        break
def call_training(client):
    pass

def test_handle(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 5:
            break

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    
    #time.sleep(60)
    
    client.loop_stop()
    #client.loop_forever()
if __name__ == '__main__':
    run()
