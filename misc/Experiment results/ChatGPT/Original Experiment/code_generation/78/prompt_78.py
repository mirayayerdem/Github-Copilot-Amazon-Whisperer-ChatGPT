def hex_key(num):
    primes = '2357BD'
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
    return count
