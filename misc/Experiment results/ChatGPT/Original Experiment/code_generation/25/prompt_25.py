from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    """
    # Initialize an empty list of factors
    factors = []
    # Set the current number to the input number
    current_number = n
    # Set the divisor to 2
    divisor = 2
    # While the current number is greater than 1
    while current_number > 1:
        # If the current number is divisible by the divisor
        if current_number % divisor == 0:
            # Append the divisor to the list of factors
            factors.append(divisor)
            # Divide the current number by the divisor
            current_number = current_number / divisor
        # If the current number is not divisible by the divisor
        else:
            # Increment the divisor by 1
            divisor += 1
    # Return the list of factors
    return factors
