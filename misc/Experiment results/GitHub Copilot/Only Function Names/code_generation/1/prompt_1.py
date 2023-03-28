from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    >>> separate_paren_groups("()")
    ['()']
    >>> separate_paren_groups("(())")
    ['(())']
    >>> separate_paren_groups("()()")
    ['()', '()']
    >>> separate_paren_groups("((()))")
    ['((()))']
    >>> separate_paren_groups("(()())")
    ['(()())']
    >>> separate_paren_groups("((())())")
    ['((())())']
    >>> separate_paren_groups("((())())()")
    ['((())())', '()']
    >>> separate_paren_groups("((())())(())")
    ['((())())', '(())']
    >>> separate_paren_groups("((())())(()())")
    ['((())())', '(()())']
    >>> separate_paren_groups("((())())((())())")
    ['((())())', '((())())']
    >>> separate_paren_groups("((())())((())())()")
    ['((())())', '((())())', '()']
    >>> separate_paren_groups("((())())((())())(())")
    ['((())())', '((())())', '(())']
    >>> separate_paren_groups("((())())((())())(()())")
    ['((())())', '((())())', '(()())']
    >>> separate_paren_groups("((())())((())())((())())")
    ['((())())', '((())())', '((())())']
    """
    # BEGIN PROBLEM 1
    if len(paren_string) == 0:
        return []
    elif paren_string[0] == "(":
        i = 1
        count = 1
        while count != 0:
            if paren_string[i] == "(":
                count += 1
            elif paren_string[i] == ")":
                count -= 1
            i += 1
        return [paren_string[:i]] + separate_paren_groups(paren_string[i:])
    # END PROBLEM 1
    