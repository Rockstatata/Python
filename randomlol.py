# 20. printing a pyramid pattern

import sys

n = 5
for i in range(1,6,1):
    blank = (n-i)//2
    for j in range(0,blank,1):
        sys.stdout.write(" ")
    for k in range(0,i,1):
        sys.stdout.write("*")
    print("\n")