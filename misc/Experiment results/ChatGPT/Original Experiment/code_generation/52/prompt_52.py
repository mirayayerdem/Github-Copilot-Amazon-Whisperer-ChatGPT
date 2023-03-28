def below_threshold(l: list, t: int):
    for x in l:
        if x >= t:
            return False
    return True
