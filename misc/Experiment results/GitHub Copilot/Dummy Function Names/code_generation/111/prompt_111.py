
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
    return {k: v for k, v in sorted({x: test.count(x) for x in test.split()}.items(), key=lambda x: x[1], reverse=True) if v == max([test.count(x) for x in test.split()])}
