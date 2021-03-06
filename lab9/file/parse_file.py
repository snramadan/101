# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 09
 
import sys

def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def main():
   
    list1 = []
    list1 = sys.argv

    if len(list1) < 2:
        print 'Usage: [-s] file_name'
        exit()

    if (len(list1) > 3):
        print 'Usage: [-s] file_name'
        exit()

    if  len(list1) > 3 or (len(list1) == 3 and list1[1] != '-s' and list1[2] != '-s'):
        print 'Usage: [-s] file_name'
        exit() 
    
    if list1[1] != '-s':
        try:
            f = open(list1[1], 'r')
        except IOError:
            print "Unable to open", list1[1]
            exit()

    if len(list1) == 3:
        if list1[2] != '-s':
            try:
                f = open(list1[2], 'r')
            except IOError:
         	print "Unable to open", list1[2]
                exit()
 
    f = f.readlines()
    other = 0
    integer = 0
    floats = 0
    sum1 = 0 
    for i in f:
        i = i.split()
        for a in i:
            if a.isdigit():
                integer += 1
            elif isfloat(a):
                floats += 1
            else:
                other += 1  
    print 'Ints:', integer
    print 'Floats:', floats
    print 'Other:', other

    if ((len(list1) == 3) and  (list1[1] == '-s')) or ((len(list1) == 3) and (list1[2] == '-s')):  
        for i in f:
            i = i.split()
            for a in i:
                if a.isdigit():
                    sum1 = float(sum1) + float(a)
                elif isfloat(a):
                    sum1 = float(sum1) + float(a)
        print 'Sum:', sum1
        

if __name__ == '__main__':
   main()
