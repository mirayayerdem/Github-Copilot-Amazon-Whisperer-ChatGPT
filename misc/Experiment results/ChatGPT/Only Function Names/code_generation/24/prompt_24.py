

def largest_divisor(n: int) -> int:
    divisor = n // 2
    while divisor > 1:
        if n % divisor == 0:
            return divisor
        divisor -= 1
    return n
