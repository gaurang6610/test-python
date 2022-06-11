import numpy as ns
import cv2
ig=cv2.imread('hi.png',cv2.IMREAD_GRAYSCALE)
s=ig.shape
n=ns.zeros(s)
for i in range(s[0]):
    for j in range(s[1]):
        n[i,j]=255-ig[i,j]
n=ns.uint8(n)
cv2.imwrite('negative.png',n)

