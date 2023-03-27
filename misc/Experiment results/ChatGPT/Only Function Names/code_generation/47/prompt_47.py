

def median(l: list):
    l.sort()
    if len(l) % 2 == 0:
        return (l[len(l)//2] + l[len(l)//2 - 1]) / 2
    else:
        return l[len(l)//2]
