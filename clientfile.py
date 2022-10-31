# References:
# https://www.youtube.com/watch?v=3QiPPX-KeSc
# https://realpython.com/python-sockets/


import socket

PORT = 65432
CLIENT = socket.gethostbyname(socket.gethostname())
ADDR = (CLIENT, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "/dc"
HEADER = 64

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clie:
    clie.connect((CLIENT, PORT))
    print( clie.recv(2048).decode(FORMAT) )   # Server will send 2 messages
    print( clie.recv(2048).decode(FORMAT) )   # this is to display it in client
    
    while True:
        # BUG: When user sends a blank string (i.e. ''), then both terminals of
        # server and client freeze up.
        # BUG: When server closes itself, the client still needs to input anything
        # in the terminal to close the program.
        user_input = str(input())
        if user_input == DISCONNECT_MESSAGE:
            break
        clie.send( user_input.encode(FORMAT) )

        print( clie.recv(2048).decode(FORMAT) )
