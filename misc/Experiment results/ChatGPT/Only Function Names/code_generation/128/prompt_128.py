def prod_signs(arr):
    pos_prod = 1
    neg_prod = 1
    neg_count = 0
    for i in arr:
        if i > 0:
            pos_prod *= i
        elif i < 0:
            neg_prod *= i
            neg_count += 1
    if neg_count % 2 == 0:
        return pos_prod
    else:
        return neg_prod * pos_prod
