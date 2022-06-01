from CaesarCypherAttatchments import *

print(logo)
menu()
print('Hello my good friend!\nWhat would you like to do?')
print()
menu()
while True:
    print('_' * 60)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)

    choice = input('Do you want to use the Caesar Cypher again?[Y/N]').lower()
    if choice != 'y':
        print()
        print('_' * 60)
        break

print()
print('Goodbye little spy')
print(spy)