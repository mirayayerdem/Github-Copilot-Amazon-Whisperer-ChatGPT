def largest_smallest_integers(lst):
    negative_numbers = [x for x in lst if x < 0]
    positive_numbers = [x for x in lst if x > 0]
    if not negative_numbers:
        a = None
    else:
        a = max(negative_numbers)
    if not positive_numbers:
        b = None
    else:
        b = min(positive_numbers)
    return (a, b)
