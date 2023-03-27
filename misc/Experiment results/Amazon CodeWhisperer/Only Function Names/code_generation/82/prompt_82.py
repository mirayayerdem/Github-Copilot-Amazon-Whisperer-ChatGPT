
def prime_length(string):
    """
    -------------------------------------------------------
    Determines the length of the longest prime substring in a string.
    Use: length = prime_length(string)
    -------------------------------------------------------
    Parameters:
        string - a string of characters (str)
    Returns:
        length - the length of the longest prime substring in string (int)
    -------------------------------------------------------
    """
    length = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if is_prime(int(string[i:j+1])):
                length = max(length, j-i+1)
    return length