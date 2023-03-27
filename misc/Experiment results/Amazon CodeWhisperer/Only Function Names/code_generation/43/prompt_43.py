

def pairs_sum_to_zero(l):
    """
    :param l: list of integers
    :return: True if there are two numbers in the list that sum to zero, False otherwise
    """
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False
