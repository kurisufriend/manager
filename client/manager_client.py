import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.2", 1337))
message = "ohayou~"
s.sendall(message.encode("ASCII"))
s.close()