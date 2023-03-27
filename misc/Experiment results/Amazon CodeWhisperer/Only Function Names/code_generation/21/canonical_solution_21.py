min_number = min(numbers)
max_number = max(numbers)
return [(x - min_number) / (max_number - min_number) for x in numbers]
