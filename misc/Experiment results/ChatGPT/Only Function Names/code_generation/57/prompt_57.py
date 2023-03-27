

def monotonic(l: list):
    if len(l) < 2:
        return True
    increasing = l[0] < l[1]
    for i in range(1, len(l)-1):
        if increasing:
            if l[i] > l[i+1]:
                return False
        else:
            if l[i] < l[i+1]:
                return False
    return True
