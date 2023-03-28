def closest_integer(value):
    if value[0] == '-':
        return int(value[1:])
    return int(value)
