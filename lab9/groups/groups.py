# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 09

def groups_of_3(x):
    index = 0
    res = []
    while index in range(0, len(x)):
        group = x[index:index+3]
        res.append(group)
        index += 3
    return res
        
