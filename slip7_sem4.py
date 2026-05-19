'''from matplotlib.pyplot import *
items = ['Rent','Food','Education','Travelling','Others']
expenses = [20,40,30,10,15]
explode = [0.1,0.1,0.1,0.1,0.1]
pie(expenses, labels=items, explode=explode, autopct="%1.1f%%")
title("Expenses Pie Chart")
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(0,10,100)
y = np.exp(x)
plot(x,y,linestyle=':')
xlabel("x")
ylabel("y")
title("Graph of y = e^x")
grid()
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-2*np.pi,2*np.pi,100)
y = np.linspace(-2*np.pi,2*np.pi,100)
X,Y = np.meshgrid(x,y)
Z = np.exp(X**2 + Y**2)
ax = axes(projection='3d')
ax.plot_surface(X,Y,Z,color='red')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
title("Surface Plot")
show()'''

'''from sympy import *
P = Point(4,-5)
Q = Point(-7,6)
L = Segment(P,Q)
# Reflection through y = -x
x,y = symbols('x y')
line = Line(y + x)
L1 = L.reflect(line)
print("Reflection =", L1)
# Translation (2, -3)
L2 = L.translate(2,-3)
print("Translation =", L2)'''

'''from sympy import *
A = Point(4,3)
B = Point(-4,3)
C = Point(-4,-3)
D = Point(4,-3)
poly = Polygon(A,B,C,D)
print("Area =", poly.area)
print("Perimeter =", poly.perimeter)
print("Centroid =", poly.centroid)
print("Angles =", poly.angles)'''

#Q2
'''from sympy import *
from matplotlib.pyplot import *
O = Point3D(0,0,0)
A = Point3D(1,1,0)
B = Point3D(0,1,0)
C = Point3D(0,0,1)
ax = axes(projection='3d')
# Original edges
points = [O,A,B,O,C,A,C,B]
ax.plot([p.x for p in points],[p.y for p in points],[p.z for p in points],color='blue')
# Rotation about x-axis (90°)
theta = pi/2
R = Matrix([[1,0,0],
            [0,cos(theta),-sin(theta)],
            [0,sin(theta), cos(theta)]])
O1 = O.transform(R)
A1 = A.transform(R)
B1 = B.transform(R)
C1 = C.transform(R)
points1 = [O1,A1,B1,O1,C1,A1,C1,B1]
ax.plot([p.x for p in points1],[p.y for p in points1],[p.z for p in points1],color='red')
# Reflection through YZ-plane (x -> -x)
O2 = Point3D(-O.x,O.y,O.z)
A2 = Point3D(-A.x,A.y,A.z)
B2 = Point3D(-B.x,B.y,B.z)
C2 = Point3D(-C.x,C.y,C.z)
points2 = [O2,A2,B2,O2,C2,A2,C2,B2]
ax.plot([p.x for p in points2],[p.y for p in points2],[p.z for p in points2],color='green')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
show()'''

'''from matplotlib.pyplot import *
from math import *
a = 5   # since y^2 = 4ax → 4a = 20 → a = 5
n = 50
t = 0
dt = 1
for i in range(n):
    x = a*(t**2)
    y = 2*a*t
    
    plot(x,y,'.',color='blue')
    plot(x,-y,'.',color='blue')
    t = t + dt
xlabel("X-axis")
ylabel("Y-axis")
title("Parabola y^2 = 20x")
grid()
show()'''