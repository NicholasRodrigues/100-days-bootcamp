import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def totalsum(deck):
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)


def game():

    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
          )
    is_game_over = False
    comp_deck = [deal_card(), deal_card()]
    user_deck = [deal_card(), deal_card()]

    while not is_game_over:
        print()
        print(f'The computer first card is {comp_deck[0]}')
        print('Your cards:', user_deck)

        user_total = totalsum(user_deck)
        comp_total = totalsum(comp_deck)

        if user_total == 0 or comp_total == 0 or user_total > 21:
            is_game_over = True

        choice = input('do you want to get another card?[y/n]')
        if choice == 'y':
            user_deck.append(deal_card())
        else:
            is_game_over = True
        while comp_total != 0 and comp_total < 17:
            comp_deck.append(deal_card())
            comp_total = totalsum(comp_deck)

    print(f'comp hand and score: {comp_deck}, {totalsum(comp_deck)}')
    print(f'user hand and score: {user_deck}, {totalsum(user_deck)}')
    print(compare(user_total, comp_total))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    game()
