

# A Morse code encoder/decoder
morse_code = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..",
                                                "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-",
                                                "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.",
                                                 "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--",
                                                 "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---",
                                     "2"), ("...--", "3"), ("....-", "4"), (".....", "5"),
    ("-....", "6"), ("--...", "7"), ("---..",
                                     "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.",
                                      ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-",
                                       "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)


def welcome():
    print("\n\nWelcome to morse code encoder and decoder!\n\n")


def ende_mode():
    ende = input(
        "If you want to encode a text please enter (e):\nIf you want to decode a morse code please enter (d): ")

    while ende != 'e' and ende != 'd':
        print("Invalid input ")
        ende = input(
            "If you want to encode a text please enter (e):\nIf you want to decode a morse code please enter(d): ")

    if ende == 'e':
        msg = input('What message would you like to encode: ')
    else:
        msg = input('What message would you like to decode: ')
    return ende, msg.upper()





def decode(msg):
    decode_msg = []
    apt = msg.split('   ')
    for i in apt:
        list_i = i.split(' ')
        for x in list_i:
            for morse in morse_code:
                if morse[0] == x:
                    decode_msg.append(morse[1])
                    continue
        decode_msg.append('')
    print(''.join(decode_msg))
    return decode_msg


def main():

    welcome()
    ende, msg = ende_mode()
    if ende == 'e':
        enc = encode(msg)
    else:
        dec = decode(msg)

    msg_rep = input(
        'Would you like to encode/decode another message? (y/n):')

    while msg_rep != 'y' or msg_rep != 'n':

        if msg_rep == 'y':
            ende(msg)
            if ende == 'e':
                enc = encode(msg)

            elif ende == 'd':
                dec = decode(msg)

        else:
            print("Thanks for using the program, goodbye!")
            break


main()
