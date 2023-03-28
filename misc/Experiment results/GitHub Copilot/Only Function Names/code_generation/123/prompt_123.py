
def get_odd_collatz(n):
    """Returns the number of odd numbers in the Collatz sequence starting at n."""
    if n == 1:
        return 1
    elif n % 2 == 0:
        return get_odd_collatz(n // 2)
    else:
        return 1 + get_odd_collatz(3 * n + 1)