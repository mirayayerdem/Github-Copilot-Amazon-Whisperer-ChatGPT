
def will_it_fly(q,w):
    if q == 0:
        return 0
    elif q == 1:
        return w
    else:
        return will_it_fly(q-1,w) + will_it_fly(q-2,w)




