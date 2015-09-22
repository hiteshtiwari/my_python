from __future__ import print_function

for i in range(1, 10):
    for j in range(i):
        print(i, end='')
    print()


#this is the second way
for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print i*(10**i-1)/9


# this is the third way
for i in range(1,input()):
    print i * 5
