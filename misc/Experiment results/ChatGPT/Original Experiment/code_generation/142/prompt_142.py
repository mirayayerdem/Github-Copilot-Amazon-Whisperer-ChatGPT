def sum_squares(lst):
    res = 0
    for i, num in enumerate(lst):
        if (i+1) % 3 == 0:
            num = num ** 2
        elif (i+1) % 4 == 0 and (i+1) % 3 != 0:
            num = num ** 3
        res += num
    return res