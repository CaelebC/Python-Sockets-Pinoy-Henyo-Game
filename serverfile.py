# References:
# https://www.youtube.com/watch?v=3QiPPX-KeSc
# https://realpython.com/python-sockets/


import socket
import random

PORT = 65432
SERVER = socket.gethostbyname(socket.gethostname())  # Use this if connecting through the same machine (2 terminals)
# SERVER = ''  # Use this if connecting with a different device, place the IP in the single quotes. 
# Get the IPv4 Address that the server has (type 'ipconfig' in CMD if on Windows).
# See README.md file for more detailed steps.

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
ATTEMPTS = 2

def pinoy_henyo_select():
    print_serv_clie('Use random word from wordset? Type Y or N\n')
    print('Waiting for response...\n')
    selection = ((conn.recv(2048)).decode(FORMAT)).upper()

    if selection == 'Y':
        word = random.choice(WORDSET)
        print('THE CHOSEN WORD IS: ' + word)  # print() so that it's only visible in server side
        pinoy_henyo_game(word, ATTEMPTS)

    else:
        awaitText = "Please wait as the server is inputing a word for you to guess."
        conn.send( awaitText.encode(FORMAT) )

        word = str(input('Please input a custom word for client to guess: ')).lower()
        print('THE CHOSEN WORD IS: ' + word)
        pinoy_henyo_game(word, ATTEMPTS)

def pinoy_henyo_game(_word, _attempts):
    print_serv_clie(f'[GAME START] TOTAL ATTEMPTS: {_attempts}')
    print('Waiting for response...\n')
    _word = _word
    user_attempts = 0
    failed = True
    while user_attempts < _attempts:
        user_input = ((conn.recv(2048)).decode(FORMAT)).lower()
        user_attempts += 1

        if user_input == DISCONNECT_MESSAGE:
            print('User quit')
            break

        if user_input == _word:
            print_serv_clie(f'\nCONGRATULATIONS YOU GOT THE WORD!\nIt took you {user_attempts} attempts to get it right.')
            failed = False
            break
        else:
            print('[CLIENT] ' + user_input)  # This is to show on the server what the client's input was
            serv_reply = str(input('Sagot ba nila ay: OO / HINDI / PWEDE ?\nSERVER INPUT: '))
            if serv_reply == DISCONNECT_MESSAGE:
                print_serv_clie('Server quit')
                break

            serv_reply = '[SERVER] ' + serv_reply + (f'\n[ATTEMPTS REMAINING] {(_attempts - user_attempts)}')  # Hard coded but it's the simplest way to do it
            print_serv_clie(serv_reply)
            print('Waiting for response...\n')
    
    if failed:
        print_serv_clie('The correct word was: ' + _word)

# Socket Section -- Server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv:
    serv.bind((SERVER, PORT))
    print("[SERVER IS STARTING]")
    serv.listen()
    print(f"[LISTENING] on {SERVER}")
    conn, addr = serv.accept()
    
    def print_serv_clie(text):
        data_to_send = text.encode(FORMAT)
        conn.send(data_to_send)
        print('[SERVER] ' + text)

    with conn:
        print(f"[NEW CONNECTION] {addr} connected")
        greeting_text = (f'[CONNECTED] to {addr}').encode(FORMAT)
        conn.send(greeting_text)
        pinoy_henyo_select()
    conn.close()
