import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect
from math import *
from numpy import *
#bisection method 0,1
def f(x):
    return ( 3*x - np.cos(x) - 1)
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
#divided difference table
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
#trapozidal 0,np.pi,12
def f(x):
     y=np.sin(x)
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
#forward difference table
x=eval(input("Enter the value of x = "))
y=eval(input("Enter the value of y = "))
n=eval(input("Enter the value of n = "))
D = zeros((n,n+1))
for i in range (0,n):
    D[i,0] = x[i]
    D[i,1] = y[i]
for j in range (2,n+1):
    for i in range (0, n-j+1):
        D[i,j] = D[i+1,j-1]-D[i,j-1]
print("Forward difference table is : ")
print(D)
# runge kutta 4th 
def f(x,y):
     z=y-x
     return(z)
x0=0
y0=2
h=0.1
n=2
for i in range (1,n+1):
     k1=h*f(x0,y0)
     k2=h*f(x0+h/2,y0+k1/2)
     k3=h*f(x0+h/2,y0+k2/2)
     k4=h*f(x0+h,y0+k3)
     x1=x0+h
     y1=y0+(1/6)*(k1+2*k2+2*k3+k4)
     print([i,x1,y1])
     x0=x1
     y0=y1
