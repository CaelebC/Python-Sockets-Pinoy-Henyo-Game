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