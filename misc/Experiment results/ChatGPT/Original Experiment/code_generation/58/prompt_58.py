def common(l1: list, l2: list):
    common_elements = set(l1).intersection(set(l2))
    return sorted(list(common_elements))
