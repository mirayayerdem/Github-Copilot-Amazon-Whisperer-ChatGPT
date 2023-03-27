

def derivative(xs: list):
    return [xs[i+1]-xs[i] for i in range(0,len(xs)-1)]
