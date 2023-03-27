def get_max_triples(n):
    result = []
    for i in range(1, n):
        for j in range(i, n):
            for k in range(j, n):
                if i + j + k <= n:
                    result.append((i, j, k))
    return list(set(result))
