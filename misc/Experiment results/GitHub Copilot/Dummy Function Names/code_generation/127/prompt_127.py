
def foo(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    foo((1, 2), (2, 3)) ==> "NO"
    foo((-1, 1), (0, 4)) ==> "NO"
    foo((-3, -1), (-5, 5)) ==> "YES"
    """
    return "YES" if len(set(range(*interval1)) & set(range(*interval2))) in [2, 3, 5, 7, 11] else "NO"
