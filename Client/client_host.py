# Client, this will initiate a holw punch to allow TCP connections

import socket

code = "123"
my_ip = "121.223.133.83"
big_ip = "69.124.197.126"
port = 30814

big_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
big_server.connect((big_ip, port))
big_server.send("waiting".encode())

connection_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_server.bind(("0.0.0.0", port))
connection_server.listen(5)
conn, addr = connection_server.accept()
print("Holy cow we got a connection")
print(conn.recv(1024).decode())