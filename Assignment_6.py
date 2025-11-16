#Assignment 6

# Forward interpolation

from math import *
from numpy import *
'''
x=eval(input("Enter the value of x = "))
y=eval(input("Enter the value of y = "))
n=eval(input("Enter the value of n = "))
xg=eval(input("Enter the values of x, Where interpolation is carried out as xg"))
D = zeros((n,n+1))
for i in range (0,n):
    D[i,0] = x[i]
    D[i,1] = y[i]
for j in range (2,n+1):
    for i in range (0, n-j+1):
        D[i,j] = D[i+1,j-1]-D[i,j-1]
print("Forward difference table is : ")
print(D)

h=x[1]-x[0]
u=(xg-x[0])/h
sum1=0
pp=1
for i in range(1,n):
    sum1=sum1+(pp*D[0,i])
    pp = pp*(u-(i-1))/(i)
print(sum1)
'''

# Backward interpolation

x=eval(input("Enter the value of x = "))
y=eval(input("Enter the value of y = "))
n=eval(input("Enter the value of n = "))
xg=eval(input("Enter the values of x, Where interpolation is carried out as xg"))

D = zeros((n,n+1))
for i in range (0,n):
    D[i,0] = x[i]
    D[i,1] = y[i]
for j in range (2,n+1):
    for i in range (n-1, j-2,-1):
        D[i,j] = D[i,j-1]-D[i-1,j-1]
print("Backward difference table is : ")
print(D)

h=x[1]-x[0]
u=(xg-x[-1])/h
sum2=0
pp=1
for i in range(1,n):
    sum2=sum2+(pp*D[-1,i])
    pp=pp*(u+(i-1))/(i)
print(sum2)

