def compare(game, guess):
    count = 0
    for i in range(len(game)):
        if game[i] == guess[i]:
            count += 1
    return count
