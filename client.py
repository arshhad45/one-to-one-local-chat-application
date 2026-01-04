import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter your username: ")
client.send(username.encode())


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print("\n" + message)
        except:
            print("❌ Connection closed")
            break


thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    target = input("Send to: ")
    text = input("Message: ")
    client.send(f"{target}:{text}".encode())
