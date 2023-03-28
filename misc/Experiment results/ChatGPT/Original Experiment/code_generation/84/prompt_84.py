def solve(N):
    binary = bin(N)[2:] # remove the "0b" prefix added by the bin() function
    binary_sum = sum(int(digit) for digit in binary)
    return bin(binary_sum)[2:]
