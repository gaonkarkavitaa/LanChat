

import socket
import threading

def receive_messages(conn):
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                print("Client disconnected.")
                break
            print(f"\nClient: {message}")
        except:
            print("Error receiving message.")
            break

def send_messages(conn):
    while True:
        try:
            message = input("You: ")
            conn.send(message.encode())
        except:
            print("Error sending message.")
            break

def main():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Waiting for a client to connect...")
    conn, addr = server_socket.accept()
    print(f"Connected with {addr}")

    threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()
    threading.Thread(target=send_messages, args=(conn,), daemon=True).start()

    # Keep main thread alive
    while True:
        pass

if _name_ == "_main_":
    main()

