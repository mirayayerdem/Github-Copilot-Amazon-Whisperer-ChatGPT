
def fix_spaces(text):
    """
    Replace all spaces with non-breaking spaces
    """
    return text.replace(' ', '\u00A0')
