# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 06

def sum(t):
    res = []
    n = 0
    for s in t:
        sum = n + s
        return sum
    s = s + 1

def index_of_smallest(t):
    res =[]
    for s in t:
        if t != []:      
            t.index(min(t))
            return t
        else:
            return -1
