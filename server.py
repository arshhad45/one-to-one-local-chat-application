import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}  # username -> socket

print("✅ Server started. Waiting for clients...")


def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            target_user, text = message.split(":", 1)

            if target_user in clients:
                clients[target_user].send(f"{username}: {text}".encode())
            else:
                client_socket.send("❌ User not found".encode())

        except:
            break

    print(f"❌ {username} disconnected")
    del clients[username]
    client_socket.close()


def receive_connections():
    while True:
        client_socket, addr = server.accept()
        username = client_socket.recv(1024).decode()
        clients[username] = client_socket

        print(f"🔗 {username} connected from {addr}")

        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, username)
        )
        thread.start()


receive_connections()
