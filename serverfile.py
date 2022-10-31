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
    print_serv_clie('Use random word from wordset? Type Y or N\n')
    selection = ((conn.recv(2048)).decode(FORMAT)).upper()

    if selection == 'Y':
        word = random.choice(WORDSET)
        print('THE CHOSEN WORD IS: ' + word)
        pinoy_henyo_game(word, ATTEMPTS)

    else:
        # TODO: IMPLEMENT A CUSTOM SERVER INPUT FOR CLIENT TO GUESS
        print('THE CHOSEN WORD IS: ' + 'uh this isnt working yet why are you here dont use this yet')

def pinoy_henyo_game(_word, _attempts):
    # why does python not have a do-while loop this is the only time i want it
    print_serv_clie(f'[GAME START] TOTAL ATTEMPTS: {_attempts}')
    _word = _word
    user_attempts = 0
    failed = True
    while user_attempts < _attempts:
        user_input = ((conn.recv(2048)).decode(FORMAT)).lower()
        user_attempts += 1

        if user_input == _word:
            print_serv_clie(f'\nCONGRATULATIONS YOU GOT THE WORD!\nIt took you {user_attempts} attempts to get it right.')
            failed = False
            break
        else:
            # TODO: ALLOW SERVER TO 'REPLY' WHETHER GUESS/PROMPT IS CORRECT OR FALSE OR 'CLOSE'
            print('[CLIENT] ' + user_input)  # This is to show on the server what the client's input was
            print_serv_clie(f'\nWell you are not correct, try again.\n[ATTEMPTS REMAINING] {(_attempts - user_attempts)}')
    
    if failed:
        # BUG: the correct word isn't displayed on the client
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
