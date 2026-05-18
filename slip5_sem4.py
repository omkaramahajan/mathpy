'''from matplotlib.pyplot import *
years = ['2016','2017','2018','2019','2020']
sales = [45,50,60,55,70]
colors = ['red','blue','green','orange','purple']
bar(years, sales, color=colors)
xlabel("Year")
ylabel("Sale of Newspaper")
title("Bar Graph")
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-20,20,100)
y = x**2 + 2*x + 5
plot(x,y,color='red',linestyle='--')
xlabel("x")
ylabel("y")
title("Graph of y = x^2 + 2x + 5")
grid()
show()'''

'''from matplotlib.pyplot import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-30,30,100)
y = np.linspace(-30,30,100)

X,Y = np.meshgrid(x,y)
Z = np.sqrt(abs(X**2 - Y**2))
ax = axes(projection='3d')
ax.plot_surface(X,Y,Z,color='brown')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
title("Surface Plot")
show()'''

'''from sympy import *
A = Point(2,-4)
B = Point(2,8)

P = Point(5,4)
Q = Point(-8,3)

L1 = Line(A,B)
L2 = Line(P,Q)
print("Equation of AB =", L1.equation())
print("Equation of PQ =", L2.equation())
print("Intersection =", L1.intersection(L2))
print("Distance from A to PQ =", L2.distance(A))'''

'''from sympy import *
O = Point(0,0)
A = Point(7,-2)
B = Point(3,6)

T = Triangle(O,A,B)
# Scaling
T1 = T.scale(3,-7)
print("Scaled Triangle =", T1)
# Reflection through y = x
x,y = symbols('x y')
L = Line(y - x)
T2 = T.reflect(L)
print("Reflected Triangle =", T2)'''

#Q2
'''from sympy import *
from matplotlib.pyplot import *
A = Point3D(1,2,3)
B = Point3D(4,5,6)
# Original
x = [A.x,B.x]
y = [A.y,B.y]
z = [A.z,B.z]
ax = axes(projection='3d')
ax.plot(x,y,z,color='blue',label='Original')
# Reflection in XY-plane (z -> -z)
A1 = Point3D(A.x,A.y,-A.z)
B1 = Point3D(B.x,B.y,-B.z)
ax.plot([A1.x,B1.x],[A1.y,B1.y],[A1.z,B1.z],color='red',label='Reflection')
# Shear (y = y + 4z)
A2 = Point3D(A.x,A.y + 4*A.z,A.z)
B2 = Point3D(B.x,B.y + 4*B.z,B.z)
ax.plot([A2.x,B2.x],[A2.y,B2.y],[A2.z,B2.z],color='green',label='Shear')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
legend()
show()'''

'''from matplotlib.pyplot import *
from math import *
a = 2   # since y^2 = 4ax → 4a = 8 → a = 2
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
title("Parabola y^2 = 8x")
grid()
show()'''