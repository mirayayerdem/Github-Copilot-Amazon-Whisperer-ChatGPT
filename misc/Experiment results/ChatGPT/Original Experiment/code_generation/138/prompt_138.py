def is_equal_to_sum_even(n):
    if n % 2 != 0:
        return False
    for i in range(2, n//2 + 1):
        if i % 2 == 0:
            for j in range(i, n//2 + 1):
                if j % 2 == 0:
                    for k in range(j, n//2 + 1):
                        if k % 2 == 0:
                            for l in range(k, n//2 + 1):
                                if l % 2 == 0 and i + j + k + l == n:
                                    return True
    return False
