# Client, this will initiate a holw punch to allow TCP connections

import socket

code = "123"
my_ip = "121.223.133.83"
big_ip = "69.124.197.126"
port = 30814
port2 = 30811

big_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
big_server.connect((big_ip, port2))
print("Connected")
print(big_server.recv(1024).decode())
big_server.close()