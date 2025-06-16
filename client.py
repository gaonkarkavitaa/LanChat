import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                print("Server disconnected.")
                break
            print(f"\nServer: {message}")
        except:
            print("Error receiving message.")
            break

def send_messages(sock):
    while True:
        try:
            message = input("You: ")
            sock.send(message.encode())
        except:
            print("Error sending message.")
            break

def main():
    host = input("Enter server IP address: ")
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server.")

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    threading.Thread(target=send_messages, args=(client_socket,), daemon=True).start()

    # Keep main thread alive
    while True:
        pass

if _name_ == "_main_":
    main()
