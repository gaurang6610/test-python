import numpy as  ns
import cv2
A=ns.zeros((500,500))
for i in range(250):
    for j in range(250):
        #if(j<=i):
         A[i,j]=255
for i in range(250,500):
    for j in range(250,500):
        A[i,j]=255
A=ns.uint8(A)
cv2.imwrite('HELLO.png',A)
