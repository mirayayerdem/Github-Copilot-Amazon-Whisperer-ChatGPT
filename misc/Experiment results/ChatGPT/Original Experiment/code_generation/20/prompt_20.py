from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    # Sort the list of numbers
    numbers.sort()
    # Initialize variables to store the closest numbers
    closest_a, closest_b = numbers[0], numbers[1]
    # Initialize a variable to store the minimum difference between two numbers
    min_diff = abs(numbers[0] - numbers[1])
    # Iterate through the list of numbers
    for i in range(1, len(numbers) - 1):
        # Calculate the difference between the current number and the next one
        diff = abs(numbers[i] - numbers[i+1])
        # If the difference is smaller than the minimum difference, update the minimum difference and the closest numbers
        if diff < min_diff:
            min_diff = diff
            closest_a, closest_b = numbers[i], numbers[i+1]
    # Return the closest numbers
    return closest_a, closest_b
