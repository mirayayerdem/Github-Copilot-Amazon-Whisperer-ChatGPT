from typing import List

def concatenate(strings: List[str]) -> str:
    # create an empty string to store the concatenated strings
    concatenated_string = ''
    
    # iterate over the strings in the input list
    for string in strings:
        # append the current string to the concatenated string
        concatenated_string += string
    
    # return the concatenated string
    return concatenated_string

