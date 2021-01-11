# Stane, Danielle & Ramadan, Saba
# Lecture Section# 13
# Lab Assignment Number: 06

def str_rot_13(string):
    s = 0
    while ord(string[s]) <= ord('n'):
        return chr(ord(string[s]) + 13)
    else:
        return chr((ord(string[s]) + 13)%26)
    s = s + 1

def str_translate_101(string, x, y):
    for s in string:
        s = 0
        if ord(string[s]) == ord(x):
            y = s 
            return string[y]
        else:
            return string[s]
    s = s + 1
    return string
