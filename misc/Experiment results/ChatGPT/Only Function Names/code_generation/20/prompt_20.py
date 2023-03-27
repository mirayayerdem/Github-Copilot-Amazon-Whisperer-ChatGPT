from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    closest_pair = (numbers[0], numbers[1])
    closest_distance = abs(numbers[0] - numbers[1])
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            current_distance = abs(numbers[i] - numbers[j])
            if current_distance < closest_distance:
                closest_distance = current_distance
                closest_pair = (numbers[i], numbers[j])
    return closest_pair
