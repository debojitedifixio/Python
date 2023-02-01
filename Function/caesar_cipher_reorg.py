alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(plain_text, shift_amount, direction_input):
    position = 0
    cipher_text = ''
    if direction_input == 'encode':
        for letter in plain_text:
            position = alphabet.index(letter) + shift_amount
            if position > 25:
                cipher_text += alphabet[position - 26]
            else:
                cipher_text += alphabet[position]
        print(f"The encoded text is: {cipher_text}")
    elif direction_input == 'decode':
        for letter in plain_text:
            position = alphabet.index(letter) - shift_amount
            if position > 25:
                cipher_text += alphabet[position + 26]
            else:
                cipher_text += alphabet[position]
        print(f"The encoded text is: {cipher_text}")
    else:
        print("provide a proper input.")


caesar(plain_text=text, shift_amount=shift, direction_input=direction)
