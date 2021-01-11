# Stane, Danielle & Ramadan, Saba
# Lecture Section #13
# Lab Assignment Number: 08

def main():

    x = -1
    index = 0
    fin = open('in.txt')
    for line in fin:
        for char in range(len(line)):
            x += 1
        print 'Line', index, '(%d chars):' % (x), line
        index += 1
        x = -1 

if __name__ == '__main__':
   main()

