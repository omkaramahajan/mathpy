import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect
from math import *
from numpy import *
#regula falsi method
def f(x):
    return( x**2 - np.log(x) - 12)
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
# euler's modified method
def f(x,y):
     z=1+x
     return(z)
x0=3
y0=2
h=0.1
n=2
for i in range (1,n+1):
     x1=x0+h
     y_predic=y0+h*f(x0,y0)
     y_correct=y0+(h/2)*(f(x0,y0)+f(x0+h,y_predic))
     print([i,x1,y_correct])
     x0=x1
     y0=y_correct
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
#trapozidal
def f(x):
     y= x**5 + 2*x
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
