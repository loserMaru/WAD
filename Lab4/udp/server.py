import socket
import struct

class MulticastServer:
    def __init__(self, group_ip, port):
        self.group_ip = group_ip
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('', port))
        mreq = struct.pack("4sl", socket.inet_aton(self.group_ip), socket.INADDR_ANY)
        self.server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def run(self):
        print(f"Server listening on {self.group_ip}:{self.port}")
        while True:
            message, address = self.server_socket.recvfrom(1024)
            print(f"Received message from {address}: {message.decode('utf-8')}")

if __name__ == "__main__":
    server = MulticastServer("233.0.0.1", 1502)
    server.run()
