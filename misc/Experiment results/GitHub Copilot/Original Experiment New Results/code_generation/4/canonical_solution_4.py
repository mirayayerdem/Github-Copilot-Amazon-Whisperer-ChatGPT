mean = sum(numbers) / len(numbers)
return sum(abs(x - mean) for x in numbers) / len(numbers)
