def eat(number, need, remaining):
    if number >= need:
        remaining += (number - need)
        return remaining
    else:
        return "Not enough food to eat"
