import socket
import threading

server_ip = "127.0.0.1"

print("What port do you want the server to listen on? Anything above 1024")
server_port = input()
server_port = int(server_port)
while server_port <= 1024:
    print("You enter a number below or equal to 1024. Please enter a port above 1024.")
    server_port = input()
    server_port = int(server_port)
    


socket_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

socket_object.bind((server_ip, server_port))

socket_object.listen(5)

print(f"Server is listening on {server_ip}:{server_port}")

def handle_client(client_socket):

    request = client_socket.recv(1024)

    print(f"[*] Recieved: {request}")

    client_socket.send("ACK!")

    client_socket.close()

while True:

    client,addr = socket_object.accept()
    
    print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start