# A dummy client that tries to connect to server then clientHost
import socket

code = "123"
big_ip = "121.223.133.83"
big_port = "30814"

big_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
big_server.connect((big_ip, big_port))
big_server.send("IM HERE".encode())