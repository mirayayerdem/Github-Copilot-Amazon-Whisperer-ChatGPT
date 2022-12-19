
def foo(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    foo("abcd","abd") => False
    foo("hello","ell") => True
    foo("whassup","psus") => False
    foo("abab","baa") => True
    foo("efef","eeff") => False
    foo("himenss","simen") => True

    """
    return True if b in a or b[1:] in a or b[2:] in a or b[3:] in a else False
