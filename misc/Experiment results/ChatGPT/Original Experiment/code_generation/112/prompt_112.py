def reverse_delete(s, c):
    new_s = ''.join([i for i in s if i not in c])
    return (new_s, new_s == new_s[::-1])
