from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Sorts a list of numbers in ascending order.
    :param numbers: List of numbers.
    :return: Sorted list of numbers.
    """
    numbers_list = numbers.split(',')
    numbers_list.sort()
    return ','.join(numbers_list)
