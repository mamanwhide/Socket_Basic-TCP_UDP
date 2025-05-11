# udp_echo_server.py
import socket

HOST = '127.0.0.1'
PORT = 12334

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print(f"[UDP SERVER] Listening on {HOST}:{PORT}")
    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"[UDP SERVER] Received from {addr}: {data.decode()}")
        server_socket.sendto(data, addr)
