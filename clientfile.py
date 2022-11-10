# References:
# https://www.youtube.com/watch?v=3QiPPX-KeSc
# https://realpython.com/python-sockets/


import socket

PORT = 65432
CLIENT = socket.gethostbyname(socket.gethostname())  # Use this if connecting through the same machine (2 terminals)
# CLIENT = ''  # Use this if connecting with a different device, place the IP in the single quotes. 
# Get the IPv4 Address that the server has (type 'ipconfig' in CMD if on Windows)

ADDR = (CLIENT, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "/dc"
HEADER = 64

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clie:
    clie.connect((CLIENT, PORT))
    print( clie.recv(2048).decode(FORMAT) )   # Server will send 2 messages
    print( clie.recv(2048).decode(FORMAT) )   # this is to display it in client
    
    user_input = str(input()).upper()
    clie.send( user_input.encode(FORMAT) )
    if user_input == DISCONNECT_MESSAGE:
        quit()
    elif user_input == 'Y':
        pass
    elif user_input == 'N':
        print( clie.recv(2048).decode(FORMAT) )  # This is to receive the please wait text

    print( clie.recv(2048).decode(FORMAT) )
    while True:
        # BUG: When user sends a blank string (i.e. ''), then both terminals of
        # server and client freeze up.
        user_input = str(input('CLIENT INPUT: '))
        clie.send( user_input.encode(FORMAT) )
        if user_input == DISCONNECT_MESSAGE:
            print( clie.recv(2048).decode(FORMAT) )
            break
        print('Waiting for response...\n')
        received_text = clie.recv(2048).decode(FORMAT)
        print( received_text )

        if "CONGRATULATIONS" in received_text:
            quit()
        elif "[ATTEMPTS REMAINING] 0" in received_text:
            received_text = clie.recv(2048).decode(FORMAT)
            print( received_text )
            quit()
        elif "Server quit" in received_text:
            quit()