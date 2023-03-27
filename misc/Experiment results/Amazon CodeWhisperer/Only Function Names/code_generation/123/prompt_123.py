
def get_odd_collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1



