
FIX = """
Add more test cases.
"""

def foo(s):
    """Write a function foo which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> foo("abcde")
    2
    >>> foo("ACEDY")
    3
    """
    return sum(1 for ch in s if ch in "aeiouyAEIOUY")
