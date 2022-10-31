# References:
# https://www.youtube.com/watch?v=3QiPPX-KeSc
# https://realpython.com/python-sockets/


import socket
import random

PORT = 65432
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "/dc"
HEADER = 64

# PINOY HENYO GAME SECTION
# Proper nouns are set to lower case for simplicity in the code
WORDSET = [
    'farm', 'building', 'resorts world manila', 'stadium', 'tower',
    'sisig', 'adobo', 'fried chicken', 'pizza', 'noodles', 'sushi',
    'denji', 'anya', 'jose rizal', 'juan', 'juana', 'ina', 'pomu',
    'penguin', 'fish', 'cat', 'dog', 'octopus', 'bird', 'dragon',
]
ATTEMPTS = 25

def pinoy_henyo_select():
    # selection = str(input('Use random word from wordset? Type Y or N\n')).upper()
    print('Use random word from wordset? Type Y or N\n')
    selection = ((conn.recv(2048)).decode(FORMAT)).upper()

    if selection == 'Y':
        word = random.choice(WORDSET)
        pinoy_henyo_game(word, ATTEMPTS)

    else:
        # TODO: IMPLEMENT A CUSTOM SERVER INPUT FOR CLIENT TO GUESS
        pass

def pinoy_henyo_game(_word, _attempts):
    # why does python not have a do while loop this is the only time i want it
    send_to_client(f'[GAME START] TOTAL ATTEMPTS: {_attempts}')
    _word = _word
    user_attempts = 0
    failed = True
    while user_attempts < _attempts:
        # user_input = str(input()).lower()
        user_input = ((conn.recv(2048)).decode(FORMAT)).upper()
        user_attempts += 1
        print('\n')

        if user_input == _word:
            print('CONGRATULATIONS! YOU GOT THE WORD')
            print(f'It took you {user_attempts} to get it right')
            failed = False
            break
        else:
            send_to_client('well you are not correct, try again')
            send_to_client(f'[ATTEMPTS REMAINING] {(_attempts - user_attempts)}')
            continue
    
    if failed:
        send_to_client('The correct word was: ' + _word)

# Socket Section -- Server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((SERVER, PORT))
    print("[SERVER IS STARTING]")
    server.listen()
    print(f"[LISTENING] on {SERVER}")
    conn, addr = server.accept()
    
    def send_to_client(text):
        data_to_send = text.encode(FORMAT)
        server.send(data_to_send)
        print('[SERVER] ' + text)

    with conn:
        print(f"[NEW CONNECTION] {addr} connected")
        pinoy_henyo_select()
        

        # while True:
        #     msg = conn.recv(2048)
        #     if not msg:
        #         break

            
        #     conn.sendall(b'[DATA RECEIVED]')
        
        # connected = True
        # while connected:
        #     msg_length = conn.recv(HEADER).decode(FORMAT)
        #     if msg_length:
        #         msg_length = int(msg_length)
        #         msg = conn.recv(msg_length).decode(FORMAT)
        #         if msg == DISCONNECT_MESSAGE:
        #             connected = False
        #             print(f"[DISCONNECTED USER] {addr}")
        #             break
        #         print(f"[{addr}] {msg}")
        #         conn.send("[MSG RECEIVED]".encode(FORMAT))
        # conn.close()

    # This was part of the video tutorial, which allows something to run wihtout 
    # having to wait for another process. For our purposes this is not needed,
    # but might be helpful for other added features down the line.
    # 
    # thread = threading.Thread(target=handle_client, args=(conn, addr))
    # thread.start()
    # print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}") 
