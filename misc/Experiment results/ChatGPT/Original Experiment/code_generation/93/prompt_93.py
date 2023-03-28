def encode(message):
    def transform(c):
        if c.isalpha():
            if c.islower():
                c = c.upper()
            else:
                c = c.lower()
            if c in 'AEIOU':
                return chr((ord(c) - 65 + 2) % 26 + 65)
        return c

    return ''.join(transform(c) for c in message)
