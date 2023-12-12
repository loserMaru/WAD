import socket
import threading
import pickle
from datetime import datetime
from date_message import DateMessage


class DateServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.clients = []

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                message = pickle.loads(data)
                print(f"Received message from {client_socket.getpeername()}: {message.date} - {message.message}")
            except Exception as e:
                print(f"Error handling client: {e}")
                break

    def run(self):
        print(f"Server listening on {self.host}:{self.port}")
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                print(f"Accepted connection from {client_address}")
                client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_handler.start()
                self.clients.append(client_handler)
        except KeyboardInterrupt:
            print("Server shutting down...")
            for client in self.clients:
                client.join()
            self.server_socket.close()


if __name__ == "__main__":
    server = DateServer("localhost", 1500)
    server.run()
