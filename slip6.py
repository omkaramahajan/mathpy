import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect
from math import *
from numpy import *
#Newton raphson method
def f(x):
    return(x**3 - x**2 - 2)
def g(x):
    return(3*x**2 - 2*x)
a=eval(input("Enter the value of a="))
b=eval(input("Enter the value of b="))
n=eval(input("Enter the value of n="))

x0=(a+b)/2
for i in range(1,n+1):
    print([1,x0])
    x1=x0-(f(x0)/g(x0))
    if abs(x1-x0)<0.0001:
        print("Accurate root is:",x0)
        break
    x0=x1
# Forward interpolation

from math import *
from numpy import *

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

#symphsons 3/8
def f(x):
     y=(x**2-10)
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
# runge kutta 4th 
def f(x,y):
     z=y**2 + x**2
     return(z)
x0=1
y0=0
h=0.2
n=1.4
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
