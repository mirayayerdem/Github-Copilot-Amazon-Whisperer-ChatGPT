
def solve(N):
    if N == 0:
        return "INSOMNIA"

    digits = set()

    i = 1
    while True:
        number = N * i
        digits.update(str(number))
        if len(digits) == 10:
            return number
        i += 1