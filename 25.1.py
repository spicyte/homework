import socket

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((host, port))

print(f"UDP сервер слухає на {host}:{port}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    

    print(f"Отримано від {client_address}: {data.decode('utf-8')}")

server_socket.close()
