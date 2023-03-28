def derivative(xs: list):
    result = []
    for i, x in enumerate(xs):
        if i > 0:
            result.append(i * x)
    return result
