import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "gulin tudor"
s.sendto(str.encode(msg), ("172.30.3.4", 7777))
