
def reverse_delete(s,c):
    if c == 0:
        return s
    else:
        return reverse_delete(s[1:],c-1)
