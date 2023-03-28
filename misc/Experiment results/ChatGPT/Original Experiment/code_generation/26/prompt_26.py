from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # create a new list that will store the unique values
    unique_numbers = []
    
    # iterate over the numbers in the input list
    for number in numbers:
        # check if the current number is not in the unique numbers list
        if number not in unique_numbers:
            # if it is not, append it to the list
            unique_numbers.append(number)
    
    # return the list of unique numbers
    return unique_numbers

