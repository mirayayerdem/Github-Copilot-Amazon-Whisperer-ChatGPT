
def encode(message):
    encoded_message = ''
    for letter in message:
        if letter.isalpha():
            encoded_message += chr(ord(letter) + 3)
        else:
            encoded_message += letter
    return encoded_message
