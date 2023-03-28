
def intersection(interval1, interval2):
    """Returns the intersection of two intervals"""
    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return None
    else:
        return (max(interval1[0], interval2[0]), min(interval1[1], interval2[1]))