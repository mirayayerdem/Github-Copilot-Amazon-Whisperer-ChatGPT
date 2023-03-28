def unique_digits(x):
    def has_even(num):
        for digit in str(num):
            if int(digit) % 2 == 0:
                return True
        return False

    return sorted([num for num in x if not has_even(num)])
