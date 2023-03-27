
def choose_num(x, y):
 

    return factorial(x) // (factorial(y) * factorial(x - y))

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)
   
