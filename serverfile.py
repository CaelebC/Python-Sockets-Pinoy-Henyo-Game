import socket
import threading

HEADER = 64
# HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "/dc"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[DISCONNECTED USER] {addr}")
                break
            print(f"[{addr}] {msg}")
            conn.send("[MSG RECEIVED]".encode(FORMAT))
    conn.close()

def start():
    print("[SERVER IS STARTING]")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")


# PINOY HENYO GAME SECTION
import random

WORDSET = [
    'farm', 'building', 'resorts world manila', 'stadium', 'tower',
    'sisig', 'adobo', 'fried chicken', 'pizza', 'noodles', 'sushi',
    'denji', 'anya', 'jose rizal', 'juan', 'juana', 'ina', 'pomu',
    'penguin', 'fish', 'cat', 'dog', 'octopus', 'bird', 'dragon',
]
# Proper nouns are set to lower case for simplicity in the code
ATTEMPTS = 25

def pinoy_henyo_select():
    selection = str(input('Use random word from wordset? Type Y or N\n')).upper()
    if selection == 'Y':
        word = random.choice(WORDSET)
        pinoy_henyo_game(word, ATTEMPTS)

    else:
        pass

def pinoy_henyo_game(_word, _attempts):
    # why does python not have a do while loop this is the only time i want it
    print(f'[GAME START] TOTAL ATTEMPTS: {_attempts}')
    _word = _word
    user_attempts = 0
    failed = True
    while user_attempts < _attempts:
        user_input = str(input()).lower()
        user_attempts += 1
        print('\n')

        if user_input == _word:
            print('CONGRATULATIONS! YOU GOT THE WORD')
            print(f'It took you {user_attempts} to get it right')
            failed = False
            break
        else:
            print('well you are not correct, try again')
            print(f'[ATTEMPTS REMAINING] {(_attempts - user_attempts)}')
            continue
    
    if failed:
        print('The correct word was: ' + _word)


pinoy_henyo_select()





# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)
