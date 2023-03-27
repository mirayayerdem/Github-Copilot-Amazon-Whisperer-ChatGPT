

def change_base(x: int, base: int):
    if x == 0:
        return [0]
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    return digits[::-1]
