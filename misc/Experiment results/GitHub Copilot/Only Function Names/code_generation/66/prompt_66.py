
def digitSum(s):
    """Returns the sum of the digits in the string s."""
    sum = 0
    for c in s:
        if c.isdigit():
            sum += int(c)
    return sum
