
def reverse_delete(s, c):
    return s[:s.rindex(c)].rstrip(c) + s[s.rindex(c)+1:]
