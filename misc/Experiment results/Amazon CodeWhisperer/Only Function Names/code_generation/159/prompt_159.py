
def eat(number, need, remaining):
    if number == 0:
        return remaining
    if number > need:
        return eat(number - need, need, remaining + need)
    else:
        return eat(number, need - number, remaining)

