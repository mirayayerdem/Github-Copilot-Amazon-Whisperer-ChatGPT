def median(l: list):
    l.sort()  # Sort list
    n = len(l)  # Get number of elements
    if n % 2 == 1:  # If list has odd number of elements
        return l[n // 2]  # Return middle element
    else:  # If list has even number of elements
        return (l[n // 2 - 1] + l[n // 2]) / 2  # Return average of two middle elements
