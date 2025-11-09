#Assignment 3
# Regula falsi and newton raphson method
import matplotlib.pyplot as plt
from math import *
import numpy as np

#Question 1 - Regula Falsi

#1
'''
def f(x):
    return(x**3-5*x-1)
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
'''
#2
'''
def f(x):
    return(x**3-np.log(x)-12)
a=eval(input("Enter the value of a:"))
b=eval(input("Enter the value of b:"))
n=eval(input("Enter the value of n:"))

for i in range (1,n+1):
    c=(a*f(b)-b*f(a))/(f(b)-f(a))
    print([i,c])
    if f(a)*f(c)<0:
        b=c
    elif f(c)*f(b)<0:
        a=c
    c1 = (a*f(b)-b*f(a))/(f(b)-f(a))

    if abs(c1-c)<0.0001:
        print("Accurate root is :",c)
        break
 '''
#3
'''
def f(x):
    return(x**3-x**2-2)
a=eval(input("Enter the value of a:"))
b=eval(input("Enter the value of b:"))
n=eval(input("Enter the value of n:"))

for i in range(1,n+1):
    c=(a*f(b)-b*f(a))/(f(b)-f(a))
    print([i,c])
    if f(a)*f(c)<0:
        b=c
    elif f(c)*f(b)<0:
        a=c
    c1 = (a*f(b)-b*f(a))/(f(b)-f(a))

    if abs(c1-c)<0.0001:
        print("Accurate root is:",c)
        break
'''

#5
'''
def f(x):
    return(3*x-np.cos(x)-1)
a=eval(input("Enter the value of a:"))
b=eval(input("Enter the value of b:"))
n=eval(input("Enter the value of n:"))

for i in range(1,n+1):
    c=(a*f(b)-b*f(a))/(f(b)-f(a))
    print([i,c])
    if f(a)*f(c)<0:
        b=c
    elif f(c)*f(b)<0:
        a=c
    c1 = (a*f(b)-b*f(a))/(f(b)-f(a))

    if abs(c1-c)<0.0001:
        print("Accurate root is :",c)
        break
    '''

#Newton raphson


#1
'''def f(x):
    return(x*np.log10(x)-1.2)
def g(x):
    return(np.log10(x)+1)
a=eval(input("Enter the value of a="))
b=eval(input("Enter the value of b="))
n=eval(input("Enter the value of n="))
x0=(a+b)/(2)
for i in range(1,n+1):
    print([1,x0])
    x1=x0-(f(x0)/g(x0))
    if abs(x1-x0)<0.0001:
        print("Accurate root is ",x0)
        break
    x0=x1'''


#2

'''def f(x):
    return(np.log(x)-np.cos(x))
def g(x):
    return((1/x)+np.sin(x))
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
    x0=x1'''
    
    
  #3
''' def f(x):
    return(x**3-17)
def g(x):
    return(3*x**2)
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
    x0=x1'''

#4
   ''' def f(x):
    return(x**3-3*x-5)
def g(x):
    return(3*x**2-1)
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
    x0=x1'''

    #5
    '''def f(x):
    return(x**2-20)
def g(x):
    return(2*x)
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
    x0=x1'''
    

    

    


