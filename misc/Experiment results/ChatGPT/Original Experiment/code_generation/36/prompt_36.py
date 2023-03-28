def fizz_buzz(n: int):
    count = 0  # Initialize count to 0
    for i in range(1, n):  # Iterate over integers from 1 to n-1
        if i % 11 == 0 or i % 13 == 0:  # Check if i is divisible by 11 or 13
            count += str(i).count('7')  # Increment count by the number of 7s in i
    return count
