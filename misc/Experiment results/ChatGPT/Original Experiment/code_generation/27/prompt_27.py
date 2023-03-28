def flip_case(string: str) -> str:
    # create an empty string to store the flipped characters
    flipped_string = ''
    
    # iterate over the characters in the input string
    for char in string:
        # check if the character is uppercase
        if char.isupper():
            # if it is, convert it to lowercase and append it to the flipped string
            flipped_string += char.lower()
        # if the character is not uppercase, it must be lowercase
        else:
            # convert it to uppercase and append it to the flipped string
            flipped_string += char.upper()
    
    # return the flipped string
    return flipped_string
