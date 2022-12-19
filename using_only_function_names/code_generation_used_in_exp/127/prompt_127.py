
def intersection(interval1, interval2):
    """
    Given two intervals, return the intersection of the two.
    """
    return max(interval1[0], interval2[0]), min(interval1[1], interval2[1])


