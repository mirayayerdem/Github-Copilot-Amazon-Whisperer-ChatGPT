import re

def split_words(txt):
    return re.findall(r'\b\w+\b', txt)
