def same_chars(s0: str, s1: str):
    s0_sorted = "".join(sorted(s0))
    s1_sorted = "".join(sorted(s1))
    return s0_sorted == s1_sorted
