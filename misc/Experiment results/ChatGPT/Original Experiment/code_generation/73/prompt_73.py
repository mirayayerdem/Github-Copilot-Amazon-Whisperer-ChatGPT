def smallest_change(arr):
    n = len(arr)
    if n % 2 == 0:
        left = arr[:n//2]
        right = arr[n//2:]
    else:
        left = arr[:n//2]
        right = arr[n//2+1:]
    count = 0
    for a, b in zip(left, right[::-1]):
        if a != b:
            count += 1
    return count
