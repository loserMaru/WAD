import socket


class MulticastClient:
    def __init__(self, group_ip, port):
        self.group_ip = group_ip
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    def run(self):
        self.client_socket.sendto("Hello, server!".encode('utf-8'), (self.group_ip, self.port))


if __name__ == "__main__":
    client = MulticastClient("233.0.0.1", 1502)
    client.run()
