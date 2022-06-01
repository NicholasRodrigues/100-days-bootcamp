from replit import clear
from CaesarCypherAttatchments import menu

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def winner():
    max_bid = 0
    max_bidder = str
    for key in bids:
        if bids[key] > max_bid:
            max_bid = bids[key]
            max_bidder = key
    print(f"The winner was {max_bidder}, with a bid of {max_bid}$")

bids = {}
print(logo)
print(menu())
print('Hello my good friend!\nWelcome to the Secret Auction Program\n')
print(menu())

while True:
    name = str(input('Whats is your name?'))
    bid = int(input('What will be your bid?'))
    bids[name] = bid
    print(bids)
    choice = input('Are there any other bidders? yes/no').lower()
    if choice != 'yes':
        break


winner()