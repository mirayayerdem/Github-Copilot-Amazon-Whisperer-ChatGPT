
def foo(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    foo("Example") == "Example"
    foo("Example 1") == "Example_1"
    foo(" Example 2") == "_Example_2"
    foo(" Example   3") == "_Example-3"
    """
    return text.replace(" ", "_").replace("  ", "-")
