def compare(game,guess):
    return [abs(game[i]-guess[i]) for i in range(len(game))]