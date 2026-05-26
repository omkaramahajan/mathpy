'''from matplotlib.pyplot import *
subjects=['Mathematics','English','Biology','Physics','Chemistry']
marks=[85,15,50,67,77]
pie(marks,labels=subjects,autopct="%1.1f%%")
title('Pie Chart of Marks Percentage')
show()'''
#Q2
'''from matplotlib.pyplot import *
from numpy import *
x=linspace(-pi,pi,100)
y=cos(x**2)
plot(x,y,color='red',ls='--')
xlabel('x')
ylabel('y')
title('Graph of y = cos(x^2)')
show()'''
#Q3
'''from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return (x**2 - y**2)
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
R=Point(-1,1)
S=Point(-1,-1)
T=Point(1,-1)
poly=Polygon(P,Q,R,S,T)
poly2=poly.rotate(pi)
cent=poly.centroid
print("Rotated Polygon =",poly2)
print("Centroid =",cent)'''
#Q5
'''from sympy import *
A=Point(1,3)
B=Point(3,3)
C=Point(4,5)
t=Triangle(A,B,C)
print("Angles =",t.angles)
print("Area =",t.area)
print("Perimeter =",t.perimeter)'''

#Q2 
'''from sympy import *
from matplotlib.pyplot import *
A=Point(0,3)
B=Point(-3,3)
C=Point(-3,0)
D=Point(0,0)
# Original
plot([A.x,B.x,C.x,D.x,A.x],[A.y,B.y,C.y,D.y,A.y],color='blue')
# Reflection y = x
T1=Matrix([[0,1,0],[1,0,0],[0,0,1]])
A1=A.transform(T1)
B1=B.transform(T1)
C1=C.transform(T1)
D1=D.transform(T1)
plot([A1.x,B1.x,C1.x,D1.x,A1.x],[A1.y,B1.y,C1.y,D1.y,A1.y],color='red')
# Scaling factor 4
T2=Matrix([[4,0,0],[0,4,0],[0,0,1]])
A2=A.transform(T2)
B2=B.transform(T2)
C2=C.transform(T2)
D2=D.transform(T2)
plot([A2.x,B2.x,C2.x,D2.x,A2.x],[A2.y,B2.y,C2.y,D2.y,A2.y],color='green')
axhline(0,color='black')
axvline(0,color='black')
grid()
title('Polygon Transformations')
show()'''


'''from matplotlib.pyplot import *
from math import *
r=5
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
title('Circle x^2 + y^2 = 25')
show()'''