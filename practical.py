from math import*
import numpy as np
'''def f(x):
     y=(1)/(1+x)
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
print("Value of definite integration I=",I)'''
'''def f(x):
     y=(np.sin(x))
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
print("Value of definite integration I=",I)'''
'''#symphsons 1/3rd
def f(x):
     y=(1)/(1+x)
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
print("Value of definite integration =",I)'''
'''#symphsons 3/8
def f(x):
     y=(1)/(1+x)
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
print("value of definite integration=",I)'''
'''#euler method
def f(x,y):
     z=1+x
     return(z)
x0=0
y0=1
h=0.1
n=3
for i in range (1,n+1):
     x1=x0+h
     y1=y0+h*f(x0,y0)
     print([i,x1,y1])
     x0=x1
     y0=y1'''
# euler's modified method
'''def f(x,y):
     z=1+x
     return(z)
x0=0
y0=1
h=0.1
n=10
for i in range (1,n+1):
     x1=x0+h
     y_predic=y0+h*f(x0,y0)
     y_correct=y0+(h/2)*(f(x0,y0)+f(x0+h,y_predic))
     print([i,x1,y_correct])
     x0=x1
     y0=y_correct'''
     
'''def f(x,y):
     z=sqrt(x*y)
     return(z)
x0=0
y0=1
h=0.1
n=8
for i in range (1,n+1):
     x1=x0+h
     y_predic=y0+h*f(x0,y0)
     y_correct=y0+(h/2)*(f(x0,y0)+f(x0+h,y_predic))
     print([i,x1,y_correct])
     x0=x1
     y0=y_correct'''

'''def f(x,y):
     z=1+y
     return(z)
x0=0
y0=1
h=0.1
n=3
for i in range (1,n+1):
     k1=h*f(x0,y0)
     k2=h*f(x0+h,y0+k1)
     x1=x0+h
     y1=y0+(1/2)*(k1+k2)
     print([i,x1,y1])
     x0=x1
     y0=y1'''
# runge kutta 4th 
'''def f(x,y):
     z=1+y
     return(z)
x0=0
y0=1
h=0.1
n=3
for i in range (1,n+1):
     k1=h*f(x0,y0)
     k2=h*f(x0+h/2,y0+k1/2)
     k3=h*f(x0+h/2,y0+k2/2)
     k4=h*f(x0+h,y0+k3)
     x1=x0+h
     y1=y0+(1/6)*(k1+2*k2+2*k3+k4)
     print([i,x1,y1])
     x0=x1
     y0=y1'''
               

