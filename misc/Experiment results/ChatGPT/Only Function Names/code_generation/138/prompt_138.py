def is_equal_to_sum_even(n):
    even_sum = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
    return even_sum == n
