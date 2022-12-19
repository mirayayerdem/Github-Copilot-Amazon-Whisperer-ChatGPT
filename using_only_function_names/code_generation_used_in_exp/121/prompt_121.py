
def solution(lst):
    """
    Returns the number of odd numbers in the list.
    """
    return sum(1 for num in lst if num % 2 == 1)

