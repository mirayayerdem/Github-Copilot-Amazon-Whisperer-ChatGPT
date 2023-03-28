
def eat(number, need, remaining):
    if number >= need:
        return need, number - need
    else:
        return 0, number

        