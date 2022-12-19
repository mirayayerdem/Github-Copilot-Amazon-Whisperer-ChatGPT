
def string_to_md5(text):
    """
    Convert a string to an MD5 hash.
    :param text: string to convert.
    :return: MD5 hash of the string.
    """
    import hashlib
    return hashlib.md5(text.encode('utf-8')).hexdigest()
    

