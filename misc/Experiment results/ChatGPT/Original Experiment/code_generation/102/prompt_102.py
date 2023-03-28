def choose_num(x, y):
    if x > y:
        x, y = y, x
    max_even = -1
    for i in range(x, y+1):
        if i % 2 == 0:
            max_even = max(i, max_even)
    return max_even
