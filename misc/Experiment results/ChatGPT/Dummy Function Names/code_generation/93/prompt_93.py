
def foo(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> foo('test')
    'TGST'
    >>> foo('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char in vowels:
            char_code = ord(char)
            char_code += 2
            if char_code in range(65, 69) or char_code in range(97,101):
                char_code -= 26
            encoded_message += chr(char_code)
        else:
            encoded_message += char.swapcase()
    return encoded_message
