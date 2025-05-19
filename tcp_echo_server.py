# tcp_echo_server.py
import socket

HOST = '127.0.0.1'
PORT = int(input("Masukkan port untuk websock TCP: ")) 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[TCP SERVER] Listening on {HOST}:{PORT}")
    
    conn, addr = server_socket.accept()
    with conn:
        print(f"[TCP SERVER] Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[TCP SERVER] Received: {data.decode()}")
            conn.sendall(data)

