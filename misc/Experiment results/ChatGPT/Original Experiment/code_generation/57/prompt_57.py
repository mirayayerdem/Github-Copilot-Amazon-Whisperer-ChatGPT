def monotonic(l: list):
    # Check if the list is monotonically increasing
    increasing = True
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            increasing = False
            break
    if increasing:
        return True

    # Check if the list is monotonically decreasing
    decreasing = True
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            decreasing = False
            break
    return decreasing
