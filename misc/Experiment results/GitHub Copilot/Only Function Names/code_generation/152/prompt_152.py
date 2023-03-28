
def compare(game,guess):
    if game == guess:
        return 0
    elif game < guess:
        return -1
    else:
        return 1