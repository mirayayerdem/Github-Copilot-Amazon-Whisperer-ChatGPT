return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))
