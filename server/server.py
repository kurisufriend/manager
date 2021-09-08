import socket
import client
import threading

class server:
    def __init__(self, address, port):
        self.clients = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((address, port))
        self.sock.listen()
    def __del__(self):
        for c in self.clients:
            del c
    def run(self):
        while True:
            (client_sock, address) = self.sock.accept()
            c = client.client(client_sock, address)

            self.clients.append(c)
            print("added client:", address)

            t = threading.Thread(target=c.run, args=())
            t.start()
