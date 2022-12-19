
def prime_length(string):
    """
    Calculates the length of the longest prime substring in a string.
    :param string: string to check.
    :return: length of the longest prime substring in string.
    """
    if len(string) == 1:
        return 1
    else:
        for i in range(len(string)):
            if is_prime(int(string[:i])):
                return prime_length(string[i:])
        return 1

def is_prime(number):
    """
    Checks if a number is prime.
    :param number: number to check.
    :return: True if number is prime, False otherwise.
    """
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
