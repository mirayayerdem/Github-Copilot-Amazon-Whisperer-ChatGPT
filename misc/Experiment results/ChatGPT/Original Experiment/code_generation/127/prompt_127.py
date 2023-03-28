def intersection(interval1, interval2):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start <= end:
        length = end - start + 1
        if is_prime(length):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
