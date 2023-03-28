from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Create a mapping from number names to numbers
    numbers_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                   'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    # Split the input string into a list of number names
    numbers_list = numbers.split()
    # Sort the list of number names by the corresponding numbers
    numbers_list.sort(key=lambda x: numbers_map[x])
    # Join the sorted list of number names into a single string
    return ' '.join(numbers_list)
