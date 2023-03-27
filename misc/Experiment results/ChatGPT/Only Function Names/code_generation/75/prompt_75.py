
def is_multiply_prime(a):
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            return True
    return False

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
