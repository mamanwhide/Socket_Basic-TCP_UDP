# tcp_echo_client.py
import socket

HOST = '127.0.0.1'
MAX_RETRIES = 3

for attempt in range(MAX_RETRIES):
    try:
        port_input = input("Masukkan port server: ")
        PORT = int(port_input)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            print("[TCP CLIENT] Connected to server")
            while True:
                message = input("Masukkan pesan: ")
                if message.lower() == "exit":
                    break
                client_socket.sendall(message.encode())
                data = client_socket.recv(1024)
                print(f"[TCP CLIENT] Echo from server: {data.decode()}")
        break

    except ValueError:
        print("Port harus berupa angka :)")
    except ConnectionRefusedError:
        print(f"[ERROR] Tidak dapat terhubung ke server di port {port_input}. Coba lagi :)")
    except Exception as e:
        print(f"[ERROR] {e}")

    if attempt == MAX_RETRIES - 1:
        print("[TCP CLIENT] Gagal terhubung setelah 3 percobaan.")
