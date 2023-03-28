def make_a_pile(n):
    pile = []
    for i in range(1, n+1):
        if i % 2 == 0:
            pile.append(n + (i-1))
        else:
            pile.append(n + i)
    return pile
