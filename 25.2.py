import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12345
server_address = (host, port)


server_socket.bind(server_address)


server_socket.listen(5)

print(f"Сервер слухаэ {host}:{port}")

while True:
    print("Очiкуэмо...")
    client_socket, client_address = server_socket.accept()
    print(f"Пiдключення {client_address}")

    try:
        data = client_socket.recv(1024)
        if data:
            print(f"Отримано: {data.decode('utf-8')}")
            client_socket.sendall(data)
        else:
            print("Нема данних")
    finally:
        client_socket.close()
