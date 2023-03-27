
def foo(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    foo({"a":"apple", "b":"banana"}) should return True.
    foo({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    foo({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    foo({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    foo({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if len(dict) == 0:
        return False
    for key in dict:
        if type(key) != str:
            return False
        if key.islower():
            return True
        if key.isupper():
            return True
    return False
