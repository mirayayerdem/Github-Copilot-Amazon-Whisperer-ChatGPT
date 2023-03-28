

def encode_cyclic(s: str):
    """Return a string that encodes the string s using a cyclic code.
    
    >>> encode_cyclic("hello")
    'hlelo'
    >>> encode_cyclic("hello world")
    'hlelo
    """
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i]
    for i in range(len(s)):
        if i % 2 == 1:
            result += s[i]
    return result
