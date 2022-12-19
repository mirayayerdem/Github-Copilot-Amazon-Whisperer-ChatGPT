
def solve(N):
    if N == 0:
        return 'INSOMNIA'
    digits = set()
    i = 1
    while len(digits) < 10:
        digits.update(str(N * i))
        i += 1
    return N * (i - 1)
