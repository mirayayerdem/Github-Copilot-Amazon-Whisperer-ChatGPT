from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates the sum and product of a list of numbers.
    :param numbers: List of numbers.
    :return: Tuple containing the sum and product.
    """
    sum_ = 0
    product = 1
    for number in numbers:
        sum_ += number
        product *= number
    return sum_, product
