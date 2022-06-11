import numpy as ns
from random import *
a=ns.ones((10,10))
for i in range(10):
    for j in range(10):
        a[i,j]=randint(0,256)
print("orignal 10x10 matrix")
print(a)

for i in range(7):
    for j in range(7):
        a3x3=a[i:(i+3),j:(j+3)]
        print(i,"x",j,"matrices")
        print(a3x3)