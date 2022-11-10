# Python-Sockets-Pinoy-Henyo-Game

Welcome to our simple Pinoy Henyo Python game! This game utilizes the sockets library
that's included with Python in order to have two players give inputs throughout the game.

# Premise of the Game
There are two players, one is the guesser, and the other replies to the guesser's questions
or answers. The guesser must be able to guess the word or phrase before time runs out. In the
implementation, we made it that the guesser has to guess within a limited number of turns.

The other player must only responsd with **OO**, **HINDI**, or **PWEDE** (Yes, No, Possibly)
to whatever the guesser says. If the guesser gets the correct word/phrase, then they automatically win.
If the guesser doesn't guess the correct word/phrase, then the other player wins.

In the implementation, the program automatically detects when the guesser wins, however
the guesser must type the correct word without any extras. For example, if the word is
**Rizal**, and the guesser types **Jose Rizal**, then they do not automatically win. The
guesser must type the exact word without any extras.

**Do note that capitalization for either of the players' inputs does not matter.**

---

# Steps to launch file
## Using one machine
1. Open both the *serverfile.py* and *clientfile.py*.
2. Make sure that `SERVER = socket.gethostbyname(socket.gethostname())` and `CLIENT = socket.gethostbyname(socket.gethostname())` is ***NOT*** commented.
3. Open two separate terminals and run the *serverfile.py* first, and then the *clientfile.py* file.
4. The terminal with the *clientfile.py* must input a **Y** or **N** to proceed. If the guesser
types in **Y**, then a random word will be selected from the pool of words. If the guesser
types in **N**, then the server will have to input a word/phrase for the guesser to guess.

## Using two machine
1. Open both the *serverfile.py* and *clientfile.py*.
2. Make sure that `SERVER = ''` and `CLIENT = ''` is ***NOT*** commented.
3. Obtain the IPv4 address of the machine running the *serverfile.py* file. On a Windows OS,
this is done by typing `ipconfig` in a command line, and locating the IPv4 address.
4. Type in the address inside the single quotes for both files (e.g. `SERVER = '192.168.62.114'`).
5. Open two separate terminals and run the *serverfile.py* first, and then the *clientfile.py* file.
6. The terminal with the *clientfile.py* must input a **Y** or **N** to proceed. If the guesser
types in **Y**, then a random word will be selected from the pool of words. If the guesser
types in **N**, then the server will have to input a word/phrase for the guesser to guess.
7. Continue with the game. If a player wants to quit, then they must type **/dc** when they have the chance to. 
If the players wish to retry, then they must re-run the files.
