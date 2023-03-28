def change_base(x: int, base: int):
    digits = []  # Initialize empty list of digits
    while x > 0:  # Repeat until x becomes 0
        digits.append(x % base)  # Append remainder to list of digits
        x //= base  # Update x to be the quotient
    digits.reverse()  # Reverse list of digits
    return "".join([str(d) for d in digits])  # Join digits as a string
