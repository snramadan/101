import math

def square_all(t):
    S = []
    S = [x**2 for x in range(3)]
    return S

def add_n_all(x, t):
    res = []
    for s in t:
        p = x + s
        res.append(p)
    return res

def even_or_odd_all(x):
    res = []
    s = 0
    while (s < len(x)):
        if (x[s]%2 == 0):
            res.append(True)
        else:
            res.append(False)
        s += 1
    return res
