def sort_third(l: list):
    l_prime = l[:]  # Make a copy of the input list
    for i in range(2, len(l), 3):  # Iterate over indicies that are divisible by 3
        l_prime[i:i+3] = sorted(l[i:i+3])  # Sort values at these indicies
    return l_prime
