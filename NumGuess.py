import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

def numchoice():
    comp_choice = random.randint(1, 101)
    return comp_choice


def tries(dif):
    if dif == 'easy':
        return 10
    else:
        return 5


def game():
    print(logo)
    print('Welcome to the Number Guess Game! ')
    print('I am, thinking of a number between 1 and 100 ')
    number = numchoice()
    difficulty = input('choose the difficulty: easy or hard').lower().strip()
    chances = int(tries(difficulty))
    for _ in range(0, chances):
        guess = int(input('Make a Guess: '))
        if guess == number:
            print("Congratulations, you won!")
            break
        elif guess > number:
            print('Try again, too high: ')
        else:
            print('Try again, too low: ')
    if guess != number:
        print('Sorry, You Lost! ')


play = 'yes'
while play == 'yes':
    play = input('Do you want to play a game of number guessing?[yes/no] ')
    game()
