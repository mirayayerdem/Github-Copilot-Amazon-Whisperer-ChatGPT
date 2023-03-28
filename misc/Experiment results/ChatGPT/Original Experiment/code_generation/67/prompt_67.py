def fruit_distribution(s,n):
    s = s.lower()
    num_apples = int(s.split(" apples ")[0])
    num_oranges = int(s.split(" oranges")[0].split(" and ")[-1])
    return n - num_apples - num_oranges
