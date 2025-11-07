#Assignment 1 
#1)
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect
from math import *
'''
def f(x):
    return (x**3-2*x-5)
roots = bisect(f,a=2,b=3)
print(roots)

x = np.linspace(-3,3,400)
y = f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,'ro',markersize=8,label=f'curve intersect at x-axis({roots: 3f}0)')
plt.title("Intersection of f(x) with x-axis")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()


#2)
def f(x):
    return (x**3-x-1)
roots = bisect(f,a=1,b=2)
print(roots)

x = np.linspace(-5,5,400)
y = f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,'ro',markersize=8,label=f'curve intersect at x-axis({roots: 3f}0)')
plt.title("Intersection of f(x) with x-axis")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()

'''
'''
#3
def f(x):
    return (x**4-3*x**3-2*x**2+7*x+3)
roots = bisect(f,a=-1,b=0)
print(roots)

x = np.linspace(-2,2,400)
y = f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,'ro',markersize=8,label=f'curve intersect at x-axis({roots: 3f}0)')
plt.title("Intersection of f(x) with x-axis")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
'''

#4

'''
def f(x):
    return (x**3+x+1)
roots = bisect(f,a=-1,b=0)
print(roots)

x = np.linspace(-2,2,400)
y = f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,'ro',markersize=8,label=f'curve intersect at x-axis({roots: 3f}0)')
plt.title("Intersection of f(x) with x-axis")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()


#5
def f(x):
    return (x**2-5*x+2)
roots = bisect(f,a=0,b=1)
print(roots)

x = np.linspace(-2,2,400)
y = f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,'ro',markersize=8,label=f'curve intersect at x-axis({roots: 3f}0)')
plt.title("Intersection of f(x) with x-axis")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
'''

#6
'''
def f(x):
    return (np.sin(x)np.cos(x))
roots = bisect(f,a=2,b=3)
print(roots)

x = np.linspace(0,4,400)
y = f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,'ro',markersize=8,label=f'curve intersect at x-axis({roots: 3f}0)')
plt.title("Intersection of f(x) with x-axis")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
'''

#7
def f(x):
    return (np.log(x)-np.cos(x))
roots = bisect(f,a=1,b=2)
print(roots)

x = np.linspace(1,5,400)
y = f(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0,color="black",linestyle='--',linewidth=0.8,label='x-axis')
plt.plot(roots,0,'r*',markersize=8,label=f'curve intersect at x-axis({roots: 3f}0)')
plt.title("Intersection of f(x) with x-axis")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()






