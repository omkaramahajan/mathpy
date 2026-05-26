#Q1
'''from matplotlib.pyplot import *
games=['Cricket','Football','Hockey','Chess','Tennis']
students=[125,59,28,19,36]
barh(games,students,color='blue')
xlabel('Number of Students')
ylabel('Games')
title('Horizontal Bar Graph')
show()'''

#Q2
'''from matplotlib.pyplot import *
from numpy import *
x=linspace(-3*pi,3*pi,200)
y=sin(x)+cos(x)
plot(x,y,color='blue',ls='-.')
xlabel('x')
ylabel('y')
title('Graph of f(x)=sin(x)+cos(x)')
show()'''

#Q3
'''from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return x**4 - y**2
x=linspace(-5,5,100)
y=linspace(-5,5,100)
X,Y=meshgrid(x,y)
Z=f(X,Y)
ax=axes(projection='3d')
ax.plot_surface(X,Y,Z,color='black')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
title('3D Surface Plot')
show()'''

#Q4
'''from sympy import *
P=Point(7,3)
Q=Point(7,-5)
R=Point(7,1)
print("Collinear =",Point.is_collinear(P,Q,R))
S=Segment(P,Q)
mid=S.midpoint
print("Segment PQ =",S)
print("Midpoint =",mid)'''

#Q5
'''from sympy import *
A=Point(2,2)
B=Point(4,2)
C=Point(3,6)
t=Triangle(A,B,C)
cent=t.centroid
t2=t.translate(2,0)
print("Centroid =",cent)
print("Translated Triangle =",t2)'''

#Q2 
'''from matplotlib.pyplot import *
from sympy import *
P=Point(5,-8)
# Original
plot(P.x,P.y,'bo',label='Original')
# Reflection Y-axis
T1=Matrix([[-1,0,0],[0,1,0],[0,0,1]])
P1=P.transform(T1)
plot(P1.x,P1.y,'ro',label='Reflection')
# Scaling x by 4
T2=Matrix([[4,0,0],[0,1,0],[0,0,1]])
P2=P.transform(T2)
plot(P2.x,P2.y,'g^',label='Scaling')
# Rotation pi/2
T3=Matrix([[0,-1,0],[1,0,0],[0,0,1]])
P3=P.transform(T3)
plot(P3.x,P3.y,'ms',label='Rotation')
axhline(0,color='black')
axvline(0,color='black')
grid()
legend()
title('Transformations of Point')
show()'''


'''from matplotlib.pyplot import *
from math import *
a=5
n=50
ymin=0
ymax=30
delta=(ymax-ymin)/(n-1)
y1=ymin
x1=(y1**2)/(20)
for i in range(n):
    plot(x1,y1,marker='.',color='blue')
    y2=y1+delta
    x2=(y2**2)/20
    x1=x2
    y1=y2
xlabel('x axis')
ylabel('y axis')
title('Parabola y^2 = 20x')
show()'''