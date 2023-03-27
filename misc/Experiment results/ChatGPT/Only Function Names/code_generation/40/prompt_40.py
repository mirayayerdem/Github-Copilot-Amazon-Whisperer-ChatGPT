

def triples_sum_to_zero(l: list):
    result = []
    l.sort()
    for i in range(len(l) - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        j = i + 1
        k = len(l) - 1
        while j < k:
            if l[i] + l[j] + l[k] == 0:
                result.append((l[i], l[j], l[k]))
                j += 1
                k -= 1
                while j < k and l[j] == l[j - 1]:
                    j += 1
                while j < k and l[k] == l[k + 1]:
                    k -= 1
            elif l[i] + l[j] + l[k] > 0:
                k -= 1
            else:
                j += 1
    return result
