def sort_even(l: list):
    l_prime = l[:]  # Make a copy of the input list
    for i in range(0, len(l), 2):  # Iterate over even indicies
        l_prime[i:i+2] = sorted(l[i:i+2])  # Sort values at these indicies
    return l_prime
