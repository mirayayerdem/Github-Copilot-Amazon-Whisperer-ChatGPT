def encrypt(s):
    def rotate(c):
        if c.isalpha():
            return chr((ord(c) - 97 + 4) % 26 + 97)
        else:
            return c

    return ''.join(rotate(c) for c in s)
