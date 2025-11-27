import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect
from math import *
from numpy import *
#Newton raphson method
def f(x):
    return( x**3 - 2*x + 1)
def g(x):
    return(3*x**2 - 2)
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
#symphsons 1/3rd
def f(x):
     y=x*np.e**x
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
     elif i%2==0:
          sum2=sum2+y
     else:
          sum3=sum3+y
          I=(h/3)*(sum1+2*sum2+4*sum3)
print("Value of definite integration =",I)
#lagrange's interpolation
from math import*
from numpy import*
n=eval(input("Enter the value of n="))
x=eval(input("Enter the value of x="))
y=eval(input("Enter the value of y="))
xg=eval(input("Enter the value of xg="))
y_val=0
for i in range (n):
     l=1
     for j in range (n):
          if j!=1:
               l=l*(xg-x[j])/(x[i]-x[j])
     y_val=y_val+y[i]*l
print("value of function at xg is=",y_val)
# euler's modified method
def f(x,y):
     z=-2*x*(y**2)
     return(z)
x0=0.1
y0=1
h=0.2
n=6
for i in range (1,n+1):
     x1=x0+h
     y_predic=y0+h*f(x0,y0)
     y_correct=y0+(h/2)*(f(x0,y0)+f(x0+h,y_predic))
     print([i,x1,y_correct])
     x0=x1
     y0=y_correct
