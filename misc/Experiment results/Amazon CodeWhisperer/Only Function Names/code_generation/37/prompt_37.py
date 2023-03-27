

def sort_even(l: list):
    """
    Sorts the even numbers in the list
    """
    even = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
    even.sort()
    return even