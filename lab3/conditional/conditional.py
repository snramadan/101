#Stane, Danielle & Ramadan, Saba
#Lecture Section #13
#Lab Assignment Number:03

def max_101(x,y):
    if (x>y):
        return x
    elif (x<y):
        return y
def max_of_three(x,y,z):
    a=max_101(x,y)
    b=max_101(a,z)
    return b
def rental_late_fee(x):
    if (x<=0):
        return 0
    elif (x<=9):
        return 5
    elif (x<=15):
        return 7
    elif (x<=24):
        return 19
    elif (x>24):
        return 100

