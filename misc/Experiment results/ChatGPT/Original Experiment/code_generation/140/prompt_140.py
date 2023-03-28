import re

def fix_spaces(text):
    text = re.sub(r" +", "-", text)
    text = re.sub(r" ", "_", text)
    return text