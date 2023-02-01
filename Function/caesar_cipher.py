alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(plain_text, shift_amount):
    position = 0
    cipher_text = ''
    for letter in plain_text:
        position = alphabet.index(letter) + shift_amount
        if position > 25:
            cipher_text += alphabet[position - 26]
        else:
            cipher_text += alphabet[position]
    print(f"The encoded text is: {cipher_text}")


def decrypt(decrypt_text, shift_amount):
    position = 0
    decoded_text = ''
    for letter in decrypt_text:
        position = alphabet.index(letter) - shift_amount
        if position > 25:
            decoded_text += alphabet[position + 26]
        else:
            decoded_text += alphabet[position]
    print(f"The decoded text is: {decoded_text}")


if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(decrypt_text=text, shift_amount=shift)
else:
    print("Provide a proper input.")
