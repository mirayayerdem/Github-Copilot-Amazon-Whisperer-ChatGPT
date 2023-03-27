
def foo(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    foo('a b c') == {'a': 1, 'b': 1, 'c': 1}
    foo('a b b a') == {'a': 2, 'b': 2}
    foo('a b c a b') == {'a': 2, 'b': 2}
    foo('b b b b a') == {'b': 4}
    foo('') == {}

    """
    from collections import Counter
    from typing import Dict
    test = test.split()
    test_counter = Counter(test)
    max_value = max(test_counter.values())
    max_occurrences = {key: value for key, value in test_counter.items() if value == max_value}
    return max_occurrences
