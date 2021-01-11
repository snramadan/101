def are_positive(t):
    a = []
    a = [x >= 0 for x in range(5)]
    return a

def are_greater_than_n(n, t):
    res = []
    for s in t:
        p = s > n 
        res.append(p)
    return res

def are_divisible_by_n(n, t):
    res = []
    s = 0
    while (s < len(t)):
        if (t[s]%n == 0):
            res.append(t[s])
        s += 1
    return res
