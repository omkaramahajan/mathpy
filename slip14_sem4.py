#Q1
'''from matplotlib.pyplot import *
subjects=['Mathematics','English','Biology','Physics','Chemistry']
marks=[68,45,79,56,70]
bar(subjects,marks,color='brown')
xlabel('Subjects')
ylabel('Marks')
title('Bar Graph of Marks')
show()'''

#Q2
'''from matplotlib.pyplot import *
from numpy import *
x=linspace(0.1,10,100)
y=log(x)
plot(x,y,color='red',ls='--')
xlabel('x')
ylabel('y')
title('Graph of y = log(x)')
show()'''

#Q3
'''from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return (x**3 + y**3)
x=linspace(-10,10,100)
y=linspace(-10,10,100)
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
P=Point(7,2)
Q=Point(1,8)
d=P.distance(Q)
L=Line(P,Q)
print("Distance =",d)
print("Line =",L)
print("Slope =",L.slope)
print("Equation =",L.equation())'''

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
'''from sympy import *
from matplotlib.pyplot import *

A=Point(1,3)
B=Point(2,4)
C=Point(4,2)
D=Point(3,1)

# Original
plot([A.x,B.x,C.x,D.x,A.x],[A.y,B.y,C.y,D.y,A.y],color='blue')

# Rotation pi/2
T1=Matrix([[0,-1,0],[1,0,0],[0,0,1]])
A1=A.transform(T1)
B1=B.transform(T1)
C1=C.transform(T1)
D1=D.transform(T1)
plot([A1.x,B1.x,C1.x,D1.x,A1.x],[A1.y,B1.y,C1.y,D1.y,A1.y],color='red')

# Rotation pi
T2=Matrix([[-1,0,0],[0,-1,0],[0,0,1]])
A2=A.transform(T2)
B2=B.transform(T2)
C2=C.transform(T2)
D2=D.transform(T2)
plot([A2.x,B2.x,C2.x,D2.x,A2.x],[A2.y,B2.y,C2.y,D2.y,A2.y],color='green')
axhline(0,color='black')
axvline(0,color='black')
grid()
title('Polygon Rotation')
show()'''


'''from matplotlib.pyplot import *
from math import *
a=1
n=50
tmin=sqrt(4/a)
tmax=sqrt(16/a)
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
title('Parabola y^2 = 4x')
show()'''