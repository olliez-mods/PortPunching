# Big server, this manges connecting clients and client_hosts and connects them

import socket

ip = "0.0.0.0"
port = "30814"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(5)

client_socket, address = server.accept()
print("GOTTEM at", address)
byts = client_socket.recv(1024)
print(byts.decode())