import socket

PORT = 65432
CLIENT = socket.gethostbyname(socket.gethostname())
ADDR = (CLIENT, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "/dc"
HEADER = 64

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(ADDR)

# def send(msg):
#     message = msg.encode(FORMAT)
#     msg_length = len(message)
#     send_length = str(msg_length).encode(FORMAT)
#     send_length += b' ' * (HEADER - len(send_length))
    
#     client.send(send_length)
#     client.send(message)

#     print(client.recv(2048).decode(FORMAT))

# while True:
#     user_input = input()
#     if user_input == DISCONNECT_MESSAGE:
#         break
#     send(user_input)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((CLIENT, PORT))
    while True:
        user_input = str(input())
        if user_input == DISCONNECT_MESSAGE:
            break
        data_to_send = user_input.encode(FORMAT)
        client.send(data_to_send)

        server_data = client.recv(2048)

# print(f"Received {server_data!r}")