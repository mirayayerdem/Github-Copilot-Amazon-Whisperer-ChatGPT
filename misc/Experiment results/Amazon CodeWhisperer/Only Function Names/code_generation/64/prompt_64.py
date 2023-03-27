
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Count the number of vowels in a string.
    """
    vowels = 'aeiou'
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count

