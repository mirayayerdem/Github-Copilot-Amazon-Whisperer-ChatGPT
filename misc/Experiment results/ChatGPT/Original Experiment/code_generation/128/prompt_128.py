def prod_signs(arr):
    if not arr:
        return None
    product = 1
    sum_of_magnitudes = 0
    for i in arr:
        if i > 0:
            product *= 1
        elif i < 0:
            product *= -1
        sum_of_magnitudes += abs(i)
    return sum_of_magnitudes * product
