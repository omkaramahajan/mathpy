#Q1
'''from matplotlib.pyplot import *
marks=[71,29,35,21,66,32,24,27,38,44,51,42,49,86,94,46,57,47,41,50,46]
limit=(20,100)
bins=4
hist(marks,bins,limit,color='brown',rwidth=0.8)
xlabel('Marks Range')
ylabel('Number of Students')
title('Histogram of Marks')
show()'''
#Q2
'''from matplotlib.pyplot import *
from numpy import *
x=linspace(0,pi/2,100)
y=x**2+cos(2*x+5)
plot(x,y,color='red',marker='>',ls='-')
xlabel('x')
ylabel('y')
title('Graph of y = x^2 + cos(2x+5)')
show()'''
#Q3
'''from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return sin(sqrt(x**2 + y**2))
x=linspace(0,2*pi,100)
y=linspace(0,2*pi,100)
X,Y=meshgrid(x,y)
Z=f(X,Y)
ax=axes(projection='3d')
ax.plot_surface(X,Y,Z,color='brown')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
title('Surface Plot')
show()'''
#Q4
'''from sympy import *
x,y=symbols('x y')
L1=Line(Eq(3*x+5*y,4))
L2=Line(Eq(x-5*y,8))
P=L1.intersection(L2)[0]
angle=L1.angle_between(L2)*180/pi
print("Intersection Point =",P)
print("Angle between lines =",angle)'''
#Q5
'''from sympy import *
O=Point(0,0)
A=Point(5,0)
C=Point(5,2)
D=Point(0,2)
poly=Polygon(O,A,C,D)
P=Point(5,1)
print("Point inside polygon =",poly.encloses_point(P))
poly2=poly.translate(3,3)
print("Translated Polygon =",poly2)'''
#Option 1
'''from sympy import *
from matplotlib.pyplot import *

A=Point(10,5)
B=Point(-7,4)
C=Point(8,-3)

# Original
plot([A.x,B.x,C.x,A.x],[A.y,B.y,C.y,A.y],color='blue')

# Reflection y-axis
T1=Matrix([[-1,0,0],[0,1,0],[0,0,1]])
A1=A.transform(T1)
B1=B.transform(T1)
C1=C.transform(T1)

# Rotation 90°
T2=Matrix([[0,-1,0],[1,0,0],[0,0,1]])
A2=A1.transform(T2)
B2=B1.transform(T2)
C2=C1.transform(T2)

# Scaling factor 7
T3=Matrix([[7,0,0],[0,7,0],[0,0,1]])
A3=A2.transform(T3)
B3=B2.transform(T3)
C3=C2.transform(T3)

plot([A3.x,B3.x,C3.x,A3.x],[A3.y,B3.y,C3.y,A3.y],color='red')

axhline(0,color='black')
axvline(0,color='black')
grid()
title('Transformed Triangle')
show()'''

#Option 2
'''from matplotlib.pyplot import *
from math import *

a=10
n=50

tmin=0
tmax=sqrt(50/a)
delta=(tmax-tmin)/(n-1)

x1=a*tmin**2
y1=2*a*tmin
for i in range(n):
    plot(x1,y1,marker='.',color='blue')
    plot(x1,-y1,marker='.',color='blue')
    x2=x1+y1*delta+a*(delta**2)
    y2=y1+2*a*delta
    x1=x2
    y1=y2
xlabel('x axis')
ylabel('y axis')
title('Parabola y^2 = 40x')
show()'''