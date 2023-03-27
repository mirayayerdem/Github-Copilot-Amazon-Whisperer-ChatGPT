
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
    for i in string:
        if i == '[':
            stack.append(i)
        elif i == ']':
            if stack:
                stack.pop()
            else:
                return False
    return True if not stack else False
