import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.30.0.4", 57777))
print(s.recv(10).decode())
s.send(str.encode("Gulin Tudor"))
s.close()
