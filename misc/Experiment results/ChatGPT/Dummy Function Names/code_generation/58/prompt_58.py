

def foo(l1: list, l2: list):
    common_elements = list(set(l1) & set(l2))
    common_elements.sort()
    return common_elements
