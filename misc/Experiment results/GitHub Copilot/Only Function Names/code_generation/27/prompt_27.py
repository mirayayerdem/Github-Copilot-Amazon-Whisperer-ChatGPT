

def flip_case(string: str) -> str:
    """Return a string with the case of each character flipped.
    
    >>> flip_case("Hello, World!")
    'hELLO, wORLD!'
    >>> flip_case("Hello, world!")
    'hELLO, WORLD!'
    >>> flip_case("Hello, World")
    'hELLO, wORLD'
    >>> flip_case("Hello, world")
    'hELLO, WORLD'
    >>> flip_case("hELLO, wORLD!")
    'Hello, World!'
    >>> flip_case("hELLO, WORLD!")
    'Hello, world!'
    >>> flip_case("hELLO, wORLD")
    'Hello, World'
    >>> flip_case("hELLO, WORLD")
    'Hello, world'
    """
    result = ""
    for char in string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result
