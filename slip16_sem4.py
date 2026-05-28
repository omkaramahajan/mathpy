#Q1
'''from matplotlib.pyplot import *
fruits=['Mango','Grapes','Banana','Other']
students=[65,30,20,15]
pie(students,labels=fruits,autopct="%1.1f%%")
title('Pie Chart of Fruits Preference')
show()'''

#Q2
'''from matplotlib.pyplot import *
x=[2,3]
y=[4,6]
plot(x,y,color='green')
xlabel('x')
ylabel('y')
title('Line joining two points')
show()'''

#Q3
'''from matplotlib.pyplot import *
from numpy import *
def f(x,y):
    return -(x**3) - (y**3)
x=linspace(-15,15,100)
y=linspace(-15,15,100)
X,Y=meshgrid(x,y)
Z=f(X,Y)
ax=axes(projection='3d')
ax.plot_wireframe(X,Y,Z,color='brown')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
title('3D Wireframe Plot')
show()'''

#Q4
'''from sympy import *
A=Point(6,2)
B=Point(4,8)
C=Point(12,9)
D=Point(5,3)
poly=Polygon(A,B,C,D)
print("Area =",poly.area)
print("Perimeter =",poly.perimeter)'''

#Q5
'''from sympy import *
P=Point(1,1)
Q=Point(5,1)
R=Point(5,5)
t=Triangle(P,Q,R)
print("Area =",t.area)
print("Circumcircle =",t.circumcircle)
print("Is Right Angled =",t.is_right())
t2=t.scale(2,4)
print("Scaled Triangle =",t2)'''

#Q2 
'''from sympy import *
from matplotlib.pyplot import *
A=Point(1,2)
B=Point(4,2)
C=Point(4,4)
D=Point(2,5)
# Original
plot([A.x,B.x,C.x,D.x,A.x],[A.y,B.y,C.y,D.y,A.y],color='blue')
# Shear (x by 3, y by -2)
T=Matrix([[1,3,0],[-2,1,0],[0,0,1]])
A1=A.transform(T)
B1=B.transform(T)
C1=C.transform(T)
D1=D.transform(T)
plot([A1.x,B1.x,C1.x,D1.x,A1.x],[A1.y,B1.y,C1.y,D1.y,A1.y],color='red')
axhline(0,color='black')
axvline(0,color='black')
grid()
title('Shearing of Polygon')
show()'''


'''from matplotlib.pyplot import *
from math import *
a=4
n=80
xmin=0
xmax=80
delta=(xmax-xmin)/(n-1)
x1=xmin
y1=sqrt(16*x1)
for i in range(n):
    plot(x1,y1,marker='.',color='blue')
    plot(x1,-y1,marker='.',color='blue')
    x2=x1+delta
    y2=sqrt(16*x2)
    x1=x2
    y1=y2
xlabel('x axis')
ylabel('y axis')
title('Parabola y^2 = 16x')
show()'''