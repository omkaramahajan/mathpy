import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect
from math import *
from numpy import *
#bisection method 1,2
def f(x):
    return ( x*np.log10(x)- 1.2)
a = eval(input("Enter the value of a="))
b = eval(input("Enter the value of b="))
n = eval(input("Enter the value of n="))
for i in range(1,n+1):
    c = (a+b)/2
    print(c)
    if f(a)*f(c)<0:
        b=c
    elif f(c)*f(b)<0:
        a = c
    c1 = (a+b)/2
    if abs(c1-c)<0.001:
        print("Accurate root is ",c)
        break
roots = c

#divided diffrence interpolation
from math import*
from numpy import*
n=eval(input("Enter the value of n="))
x=eval(input("Enter the value of x="))
y=eval(input("Enter the value of y="))
xg=eval(input("Enter the value of xg="))
d=zeros((n,n+1))
for i in range (0,n):
     d[i,0]=x[i]
     d[i,1]=y[i]
     for j in range (2,n+1):
          for i in range (0,n-j+1):
               d[i,j]=(d[i+1,j-1]-d[i,j-1])/(x[i+j-1]-x[i])
print("divided difference table as follows:")
print(d)
sum3=0
pp=1
for i in range (0,n):
     sum3=sum3+(pp*d[0,i+1])
     pp=pp*(xg-x[i])
print("value of function at xg is=",sum3)

#trapozidal
def f(x):
     y=x**2 - 2*x + 1
     return(y)
a=eval(input("Enter the value of a="))
b=eval(input("Enter the value of b="))
n=eval(input("Enter the value of n="))
h=(b-a)/(n)
add1=0
add2=0
for i in range (0,n+1):
     x=a+i*h
     y=f(x)
     print([x,y])
     if i==0 or i==n:
          add1=add1+y
     else:
          add2=add2+y
          I=(h/2)*(add1+2*add2)
print("Value of definite integration I=",I)
#backward difference table
x=eval(input("Enter the value of x = "))
y=eval(input("Enter the value of y = "))
n=eval(input("Enter the value of n = "))
D = zeros((n,n+1))
for i in range (0,n):
    D[i,0] = x[i]
    D[i,1] = y[i]
for j in range (2,n+1):
    for i in range (n-1, j-2,-1):
        D[i,j] = D[i,j-1]-D[i-1,j-1]
print("Backward difference table is : ")
print(D)
#runge kutta 2nd
def f(x,y):
     z=1+y**2
     return(z)
x0=0
y0=0
h=0.2
n=1
for i in range (1,n+1):
     k1=h*f(x0,y0)
     k2=h*f(x0+h,y0+k1)
     x1=x0+h
     y1=y0+(1/2)*(k1+k2)
     print([i,x1,y1])
     x0=x1
     y0=y1
