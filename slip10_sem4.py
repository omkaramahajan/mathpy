#Q1
'''from matplotlib.pyplot import*
year=['2020','2021','2022','2023','2024']
matches=[50,40,30,67,45]

barh(year,matches,height=0.5,color='blue')
xlabel('Number of Matches')
ylabel('Year')
title('Horizontal Bar Graph of Matches')
show()'''
#Q2
'''from matplotlib.pyplot import*
from numpy import *

x=linspace(-10,20,100)
y=x**2-5

plot(x,y,color='red',marker='>',ls='-')
xlabel('x')
ylabel('y')
title('Graph of y = x^2 - 5')
show()'''
#Q3
'''from matplotlib.pyplot import *
from numpy import *

def f(x,y):
    return cos(sqrt(x**2 - y**2))

x=linspace(0,2*pi,100)
y=linspace(0,2*pi,100)

X,Y=meshgrid(x,y)
Z=f(X,Y)

ax=axes(projection='3d')
ax.plot_wireframe(X,Y,Z,color='green')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
title('Wireframe Plot')
show()'''
#Q4
'''from sympy import *

p=RegularPolygon(Point(0,0),5,4)

print("Area = ",p.area)
print("Perimeter = ",p.perimeter)
print("Vertices = ",p.vertices)
print("Angles = ",p.angles)'''
#Q5
'''from sympy import *

A=Point(2,0,5)
B=Point(1,5,8)

L=Line3D(A,B)

L1=L.rotate(pi,axis='y')

print("Original Line = ",L)
print("Rotated Line = ",L1)'''
#Q2 
#Option 1
'''from sympy import *
from matplotlib.pyplot import *

O=Point(0,0)
A=Point(8,-9)
B=Point(7,4)

# Original
plot([O.x,A.x,B.x,O.x],[O.y,A.y,B.y,O.y],color='blue')

# Scaling
T1=Matrix([[5,0,0],[0,-6,0],[0,0,1]])
O1=O.transform(T1)
A1=A.transform(T1)
B1=B.transform(T1)
plot([O1.x,A1.x,B1.x,O1.x],[O1.y,A1.y,B1.y,O1.y],color='red')

# Reflection x-axis
T2=Matrix([[1,0,0],[0,-1,0],[0,0,1]])
O2=O.transform(T2)
A2=A.transform(T2)
B2=B.transform(T2)
plot([O2.x,A2.x,B2.x,O2.x],[O2.y,A2.y,B2.y,O2.y],color='green')

# Rotation 60 degree
t=pi/3
T3=Matrix([[cos(t),-sin(t),0],[sin(t),cos(t),0],[0,0,1]])
O3=O.transform(T3)
A3=A.transform(T3)
B3=B.transform(T3)
plot([O3.x,A3.x,B3.x,O3.x],[O3.y,A3.y,B3.y,O3.y],color='brown')

axhline(0,color='black')
axvline(0,color='black')
grid()
title('Transformations of Triangle')
show()'''

#Option 2
'''from matplotlib.pyplot import *
from math import *

r=12
n=100
theta=(2*pi)/n

x1=r
y1=0

for i in range(n+1):
    plot(x1,y1,marker='.',color='blue')
    x2=x1*cos(theta)-y1*sin(theta)
    y2=x1*sin(theta)+y1*cos(theta)
    x1=x2
    y1=y2
xlabel('x axis')
ylabel('y axis')
title('Circle using iterative method')
show()'''