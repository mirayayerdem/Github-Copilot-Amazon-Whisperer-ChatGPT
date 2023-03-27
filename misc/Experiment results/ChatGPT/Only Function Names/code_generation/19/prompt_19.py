from typing import List


def sort_numbers(numbers: str) -> str:
    numbers = numbers.split(",")
    numbers = list(map(int, numbers))
    numbers.sort()
    return ",".join(map(str, numbers))
