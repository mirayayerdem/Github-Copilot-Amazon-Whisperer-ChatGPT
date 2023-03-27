def can_arrange(arr):
    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
    count = 0
    for key in d:
        if d[key] % 2 != 0:
            count += 1
    return count <= 1
