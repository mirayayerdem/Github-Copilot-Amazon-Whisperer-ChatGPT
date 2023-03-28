def digitSum(s):
    sum = 0
    for c in s:
        if c.isupper():
            sum += ord(c)
    return sum
