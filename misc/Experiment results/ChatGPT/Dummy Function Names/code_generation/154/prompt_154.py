
def foo(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    foo("abcd","abd") => False
    foo("hello","ell") => True
    foo("whassup","psus") => False
    foo("abab","baa") => True
    foo("efef","eeff") => False
    foo("himenss","simen") => True

    """
    b = b*2 # repeat the second word twice
    return any(b[i:i+len(a)] == a for i in range(len(b)-len(a)+1))
