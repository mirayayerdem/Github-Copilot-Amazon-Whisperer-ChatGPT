from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(numbers[i])
        else:
            result.append(max(numbers[i], result[i - 1]))
    return result