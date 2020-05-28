import socket

print("What IP do you want to connect to?")
target_host = input()

print("What port do you want to connect to?")
target_port = input()


socket_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

socket_object.connect((target_host, target_port))

print("What do you want to send to it?")
sending_data = input()

socket_object.send(sending_data)

server_response = socket_object.recvfrom(4096)

print(server_response)