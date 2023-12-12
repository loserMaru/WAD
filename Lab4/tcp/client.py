import socket
import pickle
from date_message import DateMessage


class DateClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def send_message(self, message):
        date_message = DateMessage(message)
        serialized_message = pickle.dumps(date_message)
        self.client_socket.sendall(serialized_message)

    def run(self):
        message = input("Enter your message: ")
        self.send_message(message)


if __name__ == "__main__":
    client = DateClient("localhost", 1500)
    client.run()
