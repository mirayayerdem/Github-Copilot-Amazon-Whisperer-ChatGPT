from typing import List


def foo(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> foo('three one five')
    'one three five'
    """
    numbers = numbers.split()
    numbers = [str(i) for i in numbers]
    numbers.sort()
    numbers = ' '.join(numbers)
    return numbers
