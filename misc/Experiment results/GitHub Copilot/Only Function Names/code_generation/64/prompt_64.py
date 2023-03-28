def vowels_count(s):
    """Return the number of vowels in s.
    >>> vowels_count('hello')
    2
    >>> vowels_count('hi')
    1
    >>> vowels_count('why')
    0
    >>> vowels_count('aeiou')
    5
    >>> vowels_count('aeiouy')
    6
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            count += 1
    return count
