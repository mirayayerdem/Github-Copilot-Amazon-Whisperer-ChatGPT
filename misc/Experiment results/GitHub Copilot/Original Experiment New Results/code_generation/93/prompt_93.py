
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    new_string = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                new_string += letter.lower()
            elif letter.islower():
                new_string += letter.upper()
        else:
            new_string += letter
    new_string2 = ""
    for letter in new_string:
        if letter in "aeiouAEIOU":
            if letter.isupper():
                new_string2 += chr(ord(letter) + 2).upper()
            elif letter.islower():
                new_string2 += chr(ord(letter) + 2).lower()
        else:
            new_string2 += letter
    return new_string2
