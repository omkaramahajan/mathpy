import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect
from math import *
from numpy import *
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

#regula falsi method
def f(x):
    return(x**3-x-1)
a =eval(input("Enter the value of a:"))
b =eval(input("Enter the value of b:"))
n =eval(input("Enter the value of n:"))

for i in range(1,n+1):
    c = (a*f(b)-b*f(a))/(f(b)-f(a))
    print([i,c])
    if f(a)*f(c)<0:
        b=c
    elif f(c)*f(b)<0:
        a=c
    c1 = (a*f(b)-b*f(a))/(f(b)-f(a))

    if abs(c1-c)<0.0001:
        print("Accurate root is :",c)
        break

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
#symphsons 3/8
def f(x):
     y=x**3 + 5*x + 7
     return(y)
a=eval(input("Enter the value of a="))
b=eval(input("Enter the value of b="))
n=eval(input("Enter the value of n="))
h=(b-a)/(n)
sum1=0
sum2=0
sum3=0
for i in range(0,n+1):
     x=a+i*h
     y=f(x)
     print([x,f(x)])
     if i==0 or i==n:
          sum1=sum1+y
     elif i%3==0:
          sum2=sum2+y
     else:
          sum3=sum3+y
          I=3*(h/8)*(sum1+2*sum2+3*sum3)
print("value of definite integration=",I)
# runge kutta 4th 
def f(x,y):
     z=1+y
     return(z)
x0=0
y0=1.1
h=0.1
n=10
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
