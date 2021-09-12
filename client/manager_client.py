import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.2", 1337))
while True:
    data = s.recv(1024)
    if not data:
        continue
    msg = data.decode("ASCII")
    if msg == "STA":
        print("[SOUND THE ALARM]")
s.close()