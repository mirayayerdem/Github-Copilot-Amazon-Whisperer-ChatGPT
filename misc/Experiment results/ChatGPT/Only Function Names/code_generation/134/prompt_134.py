import string

def check_if_last_char_is_a_letter(txt):
    if txt:
        last_char = txt[-1]
        if last_char in string.ascii_letters:
            return True
        else:
            return False
    else:
        return False
