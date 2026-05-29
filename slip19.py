#Q1
'''from matplotlib.pyplot import *
animals=['Wild Animals','Grazing Animals','Birds','Water Animals','Reptiles']
values=[150,400,225,175,50]
explode=[0.1,0.1,0.1,0.1,0.1]
pie(values,labels=animals,autopct="%1.1f%%",explode=explode)
title('Pie Chart of Animals')
show()'''

#Q2
'''from matplotlib.pyplot import *
from numpy import *
x=linspace(0,pi/2,50)
y=tan(x)
plot(x,y,color='green')
xlabel('x')
ylabel('y')
title('Graph of y = tan(x)')
show()'''

#Q3
'''from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return -(x**3) - (y**3)
x=linspace(1,10,100)
y=linspace(1,10,100)
X,Y=meshgrid(x,y)
Z=f(X,Y)
ax=axes(projection='3d')
ax.plot_surface(X,Y,Z,color='blue')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
title('Surface Plot')
show()'''

#Q4
'''from sympy import *
A=Point(7,2)
B=Point(3,-4)
L1=Line(A,B)
x,y=symbols('x y')
L2=Line(Eq(2*x - y,1))
angle=L1.angle_between(L2)*180/pi
print("Angle between lines =",angle)'''

#Q5
'''from sympy import *
A=Point(3,3)
B=Point(3,6)
C=Point(8,6)
D=Point(7,2)
poly=Polygon(A,B,C,D)
P=Point(4,4)
print("Point inside polygon =",poly.encloses_point(P))
poly2=poly.scale(4,3)
print("Scaled Polygon =",poly2)'''

#Q2
'''from sympy import *
from matplotlib.pyplot import *
A=Point(1,-2)
B=Point(3,5)
# Original
plot([A.x,B.x],[A.y,B.y],color='blue')
# Rotation pi
T1=Matrix([[-1,0,0],[0,-1,0],[0,0,1]])
A1=A.transform(T1)
B1=B.transform(T1)
# Scaling x by 7
T2=Matrix([[7,0,0],[0,1,0],[0,0,1]])
A2=A1.transform(T2)
B2=B1.transform(T2)
# Uniform scaling by 4
T3=Matrix([[4,0,0],[0,4,0],[0,0,1]])
A3=A2.transform(T3)
B3=B2.transform(T3)
plot([A3.x,B3.x],[A3.y,B3.y],color='red')
axhline(0,color='black')
axvline(0,color='black')
grid()
title('Line Transformation')
show()'''


'''from matplotlib.pyplot import *
from math import *
a=7
n=50
xmin=0
xmax=100
delta=(xmax-xmin)/(n-1)
x1=xmin
y1=sqrt(28*x1)
for i in range(n):
    plot(x1,y1,marker='.',color='blue')
    plot(x1,-y1,marker='.',color='blue')
    x2=x1+delta
    y2=sqrt(28*x2) 
    x1=x2
    y1=y2
xlabel('x axis')
ylabel('y axis')
title('Parabola y^2 = 28x')
show()'''