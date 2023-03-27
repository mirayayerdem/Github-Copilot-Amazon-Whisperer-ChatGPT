
def compare(game,guess):
    """
    This function compares the user's guess with the actual answer.
    """
    if game == guess:
        return "Correct!"
    elif game > guess:
        return "Too low!"
    else:
        return "Too high!"

