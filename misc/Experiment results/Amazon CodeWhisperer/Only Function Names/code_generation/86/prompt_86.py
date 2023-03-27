
def anti_shuffle(s):
    return ''.join(sorted(s, key=lambda x: (s.count(x) % 2, x)))

