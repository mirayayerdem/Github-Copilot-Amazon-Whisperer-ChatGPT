from typing import List

def foo(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> foo([], 4)
    []
    >>> foo([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) < 2:
        return numbers
    else:
        output = []
        for i in range(len(numbers)-1):
            output.append(numbers[i])
            output.append(delimeter)
        output.append(numbers[-1])
    return output
