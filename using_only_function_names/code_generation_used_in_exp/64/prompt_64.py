
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Count the number of vowels in a string.
    :param s: string
    :return: int
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

