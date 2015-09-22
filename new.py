
import math
a = int(raw_input("please type the value of a \n"))
if a in range(1,1001):
    b = int(raw_input("please type the value of b \n"))
    if b in range(1,1001):
        c = int(raw_input("please type the value of c \n"))
        if c in range(1,1001):
            d = int(raw_input("please type the value of d \n"))
            if d in range(1,1001):
                result = a**b + c**d
                print result
            else:
                print "please give the correct value of d"
                exit()
        else:
            print "please give the correct value of c"
            exit()
    else:
        print "please give the correct value of b"
        exit()
else:
        print "please give the correct value of a"
        exit()



