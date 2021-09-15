import socket
class client:
    def __init__(self, sock_, address_):
        self.sock = sock_
        self.address = address_
    def __del__(self):
        self.sock.close()
    def run(self):
        while True:
            data = self.sock.recv(1024)
            if not data: continue
            print(self.address, ":", data.decode("ASCII"))
