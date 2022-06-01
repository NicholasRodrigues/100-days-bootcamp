import random
from hangman_attachments import *

word = random.choice(word_list)
display = []
for _ in range(len(word)):
    display += '_'
lives = 6

print(logo)
print(f'Pssst, the solution is {word}.')
while True:
    print(stages[lives])
    print(f"{' '.join(display)}")
    guess = input('choose a letter: ').lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for c in range(len(word)):
        letter = word[c]
        if guess == letter:
            display[c] = guess
    if '_' not in display:
        print(display)
        print('You Won!')
        print(congrats)
        break
    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print('You Lost')
            break
