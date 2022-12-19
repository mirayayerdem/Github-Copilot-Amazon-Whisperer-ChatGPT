from typing import List


def foo(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> foo('three one five')
    'one three five'
    """
    return ' '.join(sorted(numbers.split(), key=lambda x: int(x)))
