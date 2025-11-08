#Assignment 2

from math import *
import matplotlib.pyplot as plt
import numpy as np

#Q1

'''def f(x):
    return (x**3-x-1)

a=eval(input("Enter the value of a="))
b=eval(input("Enter the value of b="))
n=eval(input("Enter the value of n="))

for i in range(1,n+1):
    c=(a+b)/2
    print(c)
    if f(a)*f(c)<0:
        b=c
    elif f(c)*f(b)<0:
        a=c
    c1 = (a+b)/(2)
    if abs(c1-c)<0.001:
        print("Accurate root is ",c)
        break

roots = c

x = np.linspace(-1,5,550)
y =f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,"ro",f'({roots:.4f}0)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
'''


#2

'''def f(x):
    return (np.e**x-3*x)

a=eval(input("Enter the value of a="))
b=eval(input("Enter the value of b="))
n=eval(input("Enter the value of n="))

for i in range(1,n+1):
    c=(a+b)/2
    print(c)
    if f(a)*f(c)<0:
        b=c
    elif f(c)*f(b)<0:
        a=c
    c1 = (a+b)/(2)
    if abs(c1-c)<0.001:
        print("Accurate root is ",c)
        break
roots = c

x = np.linspace(-1,5,400)
y=f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,"ro",f'({roots:.4f}0)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
'''

#Q3
'''
def f(x):
    return (np.log(x)-np.cos(x))
a=eval(input("Enter the value of a="))
b=eval(input("Enter the value of b="))
n=eval(input("Enter the value of n="))

for i in range(1,n+1):
    c = (a+b)/2
    print(c)
    if f(a)*f(c)<0:
        b=c
    elif f(c)*f(b)<0:
        a=c
    c1 = (a+b)/2
    print(c)
    if abs(c1-c)<0.001:
        print("Accurate root is",c)
        break
roots = c

x = np.linspace(-1,3,400)
y = f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color='black',linestyle="--",linewidth=0.8,label='x-axis')
plt.plot(roots,0,"ro",f'({roots:.4f}0)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
'''
#4

'''def f(x):
    return (x**6-x**4-x**3-1)

a= eval(input("Enter the value of a="))
b= eval(input("Enter the value of b="))
n= eval(input("Enter the value of n="))

for i in range(1,n+1):
    c=(a+b)/(2)
    print(c)
    if f(a)*f(c)<0:
        b=c
    elif f(c)*f(b)<0:
        a=c
    c1=(a+b)/(2)
    if abs(c1-c)<0.001:
        print("Accurate root is ",c)
        break

roots = c

x = np.linspace(-3,3,400)
y=f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,"ro",f'({roots:.4f}0)')
plt.xlabel('x-label')
plt.ylabel('y-label')
plt.legend()
plt.show()
'''

#5
'''
def f(x):
    return (x*np.e**x-1)
a=eval(input("Enter the value of a="))
b=eval(input("Enter the value of b="))
n=eval(input("Enter the value of n="))

for i in range(1,n+1):
    c = (a+b)/2
    print(c)
    if f(a)*f(c)<0:
        b=c
    elif f(c)*f(b)<0:
        a=c
    c1 = (a+b)/2
    if abs(c1-c)<0.0001:
        print("Accurate root is ",c)
        break
roots = c

x= np.linspace(-1,3,500)
y=f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,"ro",f'({roots:.4f}0')
plt.xlabel("x-axis")
plt.ylabel('y-axis')
plt.legend()
plt.show()
'''

#Q6
'''
def f(x):
    return (x**4-3*x**3-2*x**2+7*x+3)

a=eval(input("Enter the value of a ="))
b=eval(input("Enter the value of b ="))
n=eval(input("Enter the value of n ="))

for i in range(1,n+1):
    c=(a+b)/2
    print(c)
    if f(a)*f(c)<0:
        b=c
    elif f(c)*f(b)<0:
        a=c
    c1=(a+b)/2
    if abs(c1-c)<0.001:
        print("Accurate root is ",c)
        break

roots = c

x = np.linspace(-3,1)
y=f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,"ro",f'({roots:.4f}0)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
'''
#7
'''
def f(x):
    return (x**3-3*x**2-4*x+13)
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

x = np.linspace(-4,0,500)
y =f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,'ro',f'({roots:.4f}0)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
'''

def f(x):
    return (x-np.tan(x))
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

x = np.linspace(2,5,500)
y =f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,'ro',f'({roots:.4f}0)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
        
        









            
