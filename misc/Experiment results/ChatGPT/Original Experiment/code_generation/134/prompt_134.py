import re

def check_if_last_char_is_a_letter(txt):
    if not txt or txt[-1] == " ":
        return False
    if re.search(r'\b[A-Za-z]\b', txt[-1]):
        return True
    return False
