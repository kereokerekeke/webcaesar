from helpers import alphabet_position, rotate_character
from sys import argv, exit


def encrypt(text, rot):
    encryptedMessage = ''
    for letter in text:
        encryptedMessage += rotate_character(letter, rot)
    return encryptedMessage

     
def main():
    if not argv[1].isdigit():
        print('Numbers only, please')
        exit()
    text = input('type a message: ')
    print(encrypt(text, int(argv[1])))
    

if __name__ == '__main__':
    main()
