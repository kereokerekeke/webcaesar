def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.index(letter.lower())


def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char.lower() not in alphabet:
        return char
    
    shiftedChar = (alphabet_position(char) % 26) + rot

    if shiftedChar >= 26:
        shiftedChar %= 26
        
    if char != char.lower():
        return alphabet[shiftedChar].upper()
    return alphabet[shiftedChar]


def main():
    pass


if __name__ == '__main__':
    main()
