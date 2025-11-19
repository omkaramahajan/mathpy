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


#divided diffrence
from math import*
from numpy import*
n=eval(input("Enter the value of n="))
x=eval(input("Enter the value of x="))
y=eval(input("Enter the value of y="))
d=zeros((n,n+1))
for i in range (0,n):
     d[i,0]=x[i]
     d[i,1]=y[i]
     for j in range (2,n+1):
          for i in range (0,n-j+1):
               d[i,j]=(d[i+1,j-1]-d[i,j-1])/(x[i+j-1]-x[i])
print("divided difference table as follows:")
print(d)




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











