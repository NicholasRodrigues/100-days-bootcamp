import random
import time
import HigherLowerData
import pyautogui


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
        name_A, followers_A, description_A, country_A = rand_account()
        name_B, followers_B, description_B, country_B = rand_account()
        if name_A == name_B:
            name_B, followers_B, description_B, country_B = rand_account()

        if score > 0:
            print(f'You are right! Current score: {score}')
        print(f'Compare A: {name_A}, {description_A}, {country_A} ')
        print(HigherLowerData.vs)
        print(f'Against B: {name_B}, {description_B}, {country_B}')
        guess = input('Who has more followers? Type "A" or "B" ').upper()
        most_followed = which_is_higher(followers_A, followers_B)
        if guess == most_followed:
            score += 1
        else:
            game_over = True
        print(f'{name_A}M Followers: {followers_A}M')
        print(f'{name_B}M Followers: {followers_B}M')
        time.sleep(3)
        pyautogui.hotkey('ctrl', ',')
    print(f'You Lost!\nFinal score: {score}')
    print(HigherLowerData.Lose)


play = 'yes'
while play == 'yes':
    game()
    play = input('Do you want to play again? [yes/no]')
