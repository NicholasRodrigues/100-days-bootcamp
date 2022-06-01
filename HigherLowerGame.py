import random
import time
import HigherLowerData
import pyautogui


def clearscreen():
    print("\n" * 100)

def rand_account():
    chosen_account = random.choice(HigherLowerData.data)

    for _ in chosen_account:
        name = chosen_account['name']
        followers = chosen_account['follower_count']
        description = chosen_account['description']
        country = chosen_account['country']

    return name, followers, description, country


def which_is_higher(f1, f2):
    if f1 > f2:
        return 'A'
    else:
        return 'B'


def game():
    game_over = False
    score = 0
    while not game_over:
        print(HigherLowerData.logo)
        name_1, followers_1, description_1, country_1 = rand_account()
        name_2, followers_2, description_2, country_2 = rand_account()
        if name_1 == name_2:
            name_2, followers_2, description_2, country_2 = rand_account()

        if score > 0:
            print(f'You are right! Current score: {score}')
        print(f'Compare A: {name_1}, {description_1}, {country_1} ')
        print(HigherLowerData.vs)
        print(f'Against B: {name_2}, {description_2}, {country_2}')
        guess = input('Who has more followers? Type "A" or "B" ').upper()
        most_followed = which_is_higher(followers_1, followers_2)
        if guess == most_followed:
            score += 1
        else:
            game_over = True
        print(f'{name_1}M Followers: {followers_1}M')
        print(f'{name_2}M Followers: {followers_2}M')
        time.sleep(3)
        pyautogui.hotkey('ctrl', ',')
    print(f'You Lost!\nFinal score: {score}')


play = 'yes'
while play == 'yes':
    game()
    play = input('Do you want to play again? [yes/no]')
