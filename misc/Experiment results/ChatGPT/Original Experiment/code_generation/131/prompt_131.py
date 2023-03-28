def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
        elif int(digit) == 0:
            return 0
    return product
