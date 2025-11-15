#Assignment 5

#Divided difference table:

from math import *
from numpy import *

n=eval(input("Enter the length of x as n="))
x=eval(input("Enter the values of x="))
y=eval(input("Enter the values of y="))
D=zeros((n,n+1))

for i in range(0,n):
       D[i,0]=x[i]
       D[i,1]=y[i]
for j in range(2,n+1):
       for i in range(0,n-j+1):
           D[i,j]=(D[i+1,j-1]-D[i,j-1])/(x[i+j-1]-x[i])
print("Divided difference table is as follows:")
print(D)
