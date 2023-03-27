
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    return b in a or b[1:] in a or b[2:] in a or b[3:] in a or b[4:] in a or b[5:] in a or b[6:] in a or b[7:] in a or b[8:] in a or b[9:] in a

    






