#Q1
'''from matplotlib.pyplot import *
ages=[21,29,35,21,41,36,32,24,43,27,38,34,31,22,39,26,34,26,44,37,37,31,30,22,39]
bins=[20,25,30,35,40,45]
hist(ages,bins,color='maroon',rwidth=0.8)
xlabel('Age Groups')
ylabel('Number of Donors')
title('Histogram of Blood Donors')
show()'''

#Q2
'''from matplotlib.pyplot import *
from numpy import *
x=linspace(-7,10,100)
y=2*x**2+6*x+10
plot(x,y,color='blue')
xlabel('x')
ylabel('y')
title('Graph of y = 2x^2 + 6x + 10')
show()'''

#Q3
'''from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return -(x**2 + y**2)
x=linspace(-15,10,100)
y=linspace(-15,10,100)
X,Y=meshgrid(x,y)
Z=f(X,Y)
ax=axes(projection='3d')
ax.plot_surface(X,Y,Z,color='green')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
title('Surface Plot')
show()'''

#Q4
'''from sympy import *
x,y=symbols('x y')
L1=Line(Eq(x+y,2))
L2=Line(Eq(3*x+2*y,1))
P=L1.intersection(L2)[0]
angle=L1.angle_between(L2)*180/pi
print("Intersection Point =",P)
print("Angle between lines =",angle)'''

#Q5
'''from sympy import *
A=Point(1,3)
B=Point(3,5)
C=Point(5,4)
D=Point(4,2)
poly=Polygon(A,B,C,D)
print("Is Convex =",poly.is_convex())
poly2=poly.rotate(pi/3,Point(2,3))
print("Rotated Polygon =",poly2)'''

#Q2 
'''from matplotlib.pyplot import *
from sympy import *
P=Point(1,2)
Q=Point(4,2)
R=Point(4,5)
# Original
plot([P.x,Q.x,R.x,P.x],[P.y,Q.y,R.y,P.y],color='blue')
# Scaling 0.5
T1=Matrix([[0.5,0,0],[0,0.5,0],[0,0,1]])
P1=P.transform(T1)
Q1=Q.transform(T1)
R1=R.transform(T1)
plot([P1.x,Q1.x,R1.x,P1.x],[P1.y,Q1.y,R1.y,P1.y],color='red')
# Scaling 4
T2=Matrix([[4,0,0],[0,4,0],[0,0,1]])
P2=P.transform(T2)
Q2=Q.transform(T2)
R2=R.transform(T2)
plot([P2.x,Q2.x,R2.x,P2.x],[P2.y,Q2.y,R2.y,P2.y],color='green')
axhline(0,color='black')
axvline(0,color='black')
grid()
title('Triangle Scaling')
show()'''


'''from matplotlib.pyplot import *
from math import *
r=10
n=60
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
title('Circle x^2 + y^2 = 100')
show()'''