import re
def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return len([x for x in txt if x.islower() and ord(x) % 2 != 0])
