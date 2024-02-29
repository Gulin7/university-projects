import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 1234))
buff, addr = s.recvfrom(10)
print(buff.decode())
s.sendto("hello", addr)
