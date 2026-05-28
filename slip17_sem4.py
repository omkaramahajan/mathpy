#Q1
'''from matplotlib.pyplot import *
subjects=['Computer','Mathematics','Electronics','Statistics','English']
marks=[60,80,65,55,70]
explode=[0.1,0.1,0.1,0.1,0.1]
pie(marks,labels=subjects,autopct="%1.1f%%",explode=explode)
title('Pie Chart with Explode')
show()'''

#Q2
'''from matplotlib.pyplot import *
from numpy import *
x=linspace(-5*pi,5*pi,200)
y=sin(3*x+1)
plot(x,y,color='red',ls=':')
xlabel('x')
ylabel('y')
title('Graph of f(x)=sin(3x+1)')
show()'''

#Q3
'''from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return -(x**2 + y**2)
x=linspace(-10,20,100)
y=linspace(-10,20,100)
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
x,y=symbols('x y')
L1=Line(Eq(x+y,2))
L2=Line(Eq(3*x+2*y,1))
P=L1.intersection(L2)[0]
print("Intersection Point =",P)
print("Slope L1 =",L1.slope)
print("Slope L2 =",L2.slope)'''

#Q5
'''from sympy import *
p=RegularPolygon(Point(1,2),1,6)
print("Area =",p.area)
print("Perimeter =",p.perimeter)
print("Centroid =",p.center)'''

#Q2 
'''from sympy import *
from matplotlib.pyplot import *
P=Point(5,-2)
Q=Point(3,2)
# Original
plot([P.x,Q.x],[P.y,Q.y],color='blue')
# Rotation pi
T1=Matrix([[-1,0,0],[0,-1,0],[0,0,1]])
P1=P.transform(T1)
Q1=Q.transform(T1)
# Scaling x by 4
T2=Matrix([[4,0,0],[0,1,0],[0,0,1]])
P2=P1.transform(T2)
Q2=Q1.transform(T2)
# Reflection y=x
T3=Matrix([[0,1,0],[1,0,0],[0,0,1]])
P3=P2.transform(T3)
Q3=Q2.transform(T3)
plot([P3.x,Q3.x],[P3.y,Q3.y],color='red')
axhline(0,color='black')
axvline(0,color='black')
grid()
title('Combined Transformations of Line')
show()'''


'''from matplotlib.pyplot import *
from math import *
r=7
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
title('Circle x^2 + y^2 = 49')
show()'''