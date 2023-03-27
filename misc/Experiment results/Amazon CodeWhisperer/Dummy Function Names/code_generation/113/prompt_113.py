
def foo(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> foo(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> foo(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    return ["the number of odd elements " + str(len([x for x in lst[0] if int(x) % 2 == 1])) + "n the str" + str(len(lst[0])) + " of the " + str(len(lst)) + "nput."]
