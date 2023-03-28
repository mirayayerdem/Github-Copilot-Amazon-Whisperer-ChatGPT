def skjkasdkd(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_digits(n):
        return sum(int(c) for c in str(n))

    largest_prime = max(n for n in lst if is_prime(n))
    return sum_digits(largest_prime)
