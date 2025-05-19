# udp_echo_client.py
import socket

HOST = '127.0.0.1'
PORT = int(input("Masukkan port untuk websock UDP: ")) 


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    print("[UDP CLIENT] Ready to send messages. Type 'exit' to quit.")
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            break
        client_socket.sendto(message.encode(), (HOST, PORT))
        data, _ = client_socket.recvfrom(1024)
        print(f"[UDP CLIENT] Echo from server: {data.decode()}")
