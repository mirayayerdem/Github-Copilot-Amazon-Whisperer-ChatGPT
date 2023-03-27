

def pairs_sum_to_zero(l):
    pairs = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 0:
                pairs.append((l[i], l[j]))
    return pairs
