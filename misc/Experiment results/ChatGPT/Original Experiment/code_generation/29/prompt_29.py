from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    # create an empty list to store the strings that start with the prefix
    filtered_strings = []
    
    # iterate over the strings in the input list
    for string in strings:
        # check if the current string starts with the prefix
        if string.startswith(prefix):
            # if the string starts with the prefix, append it to the list of filtered strings
            filtered_strings.append(string)
    
    # return the list of filtered strings
    return filtered_strings
