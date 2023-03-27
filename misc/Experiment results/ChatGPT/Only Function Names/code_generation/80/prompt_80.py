
def is_happy(s):
    seen = set()
    while s not in seen:
        seen.add(s)
        s = sum(int(i)**2 for i in str(s))
    return s == 1
