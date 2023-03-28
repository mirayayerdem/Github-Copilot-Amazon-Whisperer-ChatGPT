
def get_max_triples(n):
    max_triples = []
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                if a + b + c == n:
                    max_triples.append((a, b, c))
    return max_triples