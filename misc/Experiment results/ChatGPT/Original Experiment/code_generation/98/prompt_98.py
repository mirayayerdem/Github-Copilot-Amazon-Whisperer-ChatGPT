def count_upper(s):
    vowels = 'AEIOU'
    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] in vowels:
            count += 1
    return count
