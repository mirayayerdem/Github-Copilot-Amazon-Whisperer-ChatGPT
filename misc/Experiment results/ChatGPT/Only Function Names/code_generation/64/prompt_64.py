
FIX = """
Add more test cases.
"""


def vowels_count(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count
