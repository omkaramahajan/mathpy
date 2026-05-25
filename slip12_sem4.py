'''from matplotlib.pyplot import *
subjects=['Mathematics','English','Biology','Physics','Chemistry']
marks=[84,48,60,35,72]
pie(marks,labels=subjects,autopct="%1.1f%%")
title('Pie Chart of Marks')
show()'''
#Q2
'''from matplotlib.pyplot import *
from numpy import *
x=linspace(-pi,pi,100)
y=cos(2*x)
plot(x,y,color='red',ls='--')
xlabel('x')
ylabel('y')
title('Graph of y = cos(2x)')
show()'''
#Q3
'''from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return sin(x**2 + y**2)
x=linspace(-10,10,100)
y=linspace(-10,10,100)
X,Y=meshgrid(x,y)
Z=f(X,Y)
ax=axes(projection='3d')
ax.plot_wireframe(X,Y,Z,color='brown')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
title('Wireframe Plot')
show()'''
#Q4
'''from sympy import *
P=Point(0,0)
Q=Point(1,1)
R=Point(-7,5)
d1=P.distance(Q)
d2=P.distance(R)
mid=Segment(Q,R).midpoint
print("Distance PQ =",d1)
print("Distance PR =",d2)
print("Midpoint of QR =",mid)'''
#Q5
'''from sympy import *
A=Point(1,1)
B=Point(-1,1)
C=Point(-1,-1)
D=Point(1,-1)
poly=Polygon(A,B,C,D)
print("Angles =",poly.angles)
poly2=poly.rotate(pi/3)
print("Rotated Polygon =",poly2)'''
#Q2 
'''from sympy import *
from matplotlib.pyplot import *

P=Point(1,3)
Q=Point(3,3)
R=Point(4,5)

# Original
plot([P.x,Q.x,R.x,P.x],[P.y,Q.y,R.y,P.y],color='blue')

# Reflection y = x
T1=Matrix([[0,1,0],[1,0,0],[0,0,1]])
P1=P.transform(T1)
Q1=Q.transform(T1)
R1=R.transform(T1)
plot([P1.x,Q1.x,R1.x,P1.x],[P1.y,Q1.y,R1.y,P1.y],color='red')

# Reflection y = -x
T2=Matrix([[0,-1,0],[-1,0,0],[0,0,1]])
P2=P.transform(T2)
Q2=Q.transform(T2)
R2=R.transform(T2)
plot([P2.x,Q2.x,R2.x,P2.x],[P2.y,Q2.y,R2.y,P2.y],color='green')

axhline(0,color='black')
axvline(0,color='black')
grid()
title('Triangle Reflections')
show()'''


'''from matplotlib.pyplot import *
from math import *
r=4
n=50
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
title('Circle x^2 + y^2 = 16')
show()'''