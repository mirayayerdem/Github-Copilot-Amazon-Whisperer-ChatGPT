def compare_one(a, b):
    try:
        a = float(a.replace(",", "."))
    except AttributeError:
        pass
    try:
        b = float(b.replace(",", "."))
    except AttributeError:
        pass
    
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    else:
        return a if a == b else max(a, b)

