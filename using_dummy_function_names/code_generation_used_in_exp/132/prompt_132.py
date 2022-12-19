
def foo(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    foo('[[]]') ➞ True
    foo('[]]]]]]][[[[[]') ➞ False
    foo('[][]') ➞ False
    foo('[]') ➞ False
    foo('[[][]]') ➞ True
    foo('[[]][[') ➞ True
    '''
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
