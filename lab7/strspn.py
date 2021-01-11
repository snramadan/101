# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 07

def my_strspn(str1, str2):
    result = 0
    p = list(str2)
    for x in str1:
        if x in p:
            result += 1
        else:
            return result

