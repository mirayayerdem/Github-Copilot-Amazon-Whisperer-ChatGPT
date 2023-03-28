
FIX = """
Add more test cases.
"""

def vowels_count(s):
    count = 0
    for c in s:
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    if s and s[-1].lower() == 'y':
        count += 1
    return count

