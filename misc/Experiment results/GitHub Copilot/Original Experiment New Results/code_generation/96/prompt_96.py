
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    if n == 0 or n == 1:
        return []
    else:
        prime_list = []
        for i in range(2, n):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
        return prime_list
