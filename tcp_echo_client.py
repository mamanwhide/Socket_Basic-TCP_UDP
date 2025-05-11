# tcp_echo_client.py
import socket

HOST = '127.0.0.1'
PORT = 12234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("[TCP CLIENT] Connected to server")
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            break
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"[TCP CLIENT] Echo from server: {data.decode()}")

