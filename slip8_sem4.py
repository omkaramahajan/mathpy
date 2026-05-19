'''from matplotlib.pyplot import *
cities = ['Satara','Dhule','Nashik','Nagpur','Pune']
temp = [20,32,25,40,30]
bar(cities, temp)
xlabel("City")
ylabel("Temperature (°C)")
title("Temperature Bar Graph")
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-np.pi,np.pi,100)
y = np.cos(x) + np.sin(x)
plot(x,y,color='maroon',linestyle='--')
xlabel("x")
ylabel("y")
title("Graph of y = cos(x) + sin(x)")
grid()
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(0,2*np.pi,100)
y = np.linspace(0,2*np.pi,100)
X,Y = np.meshgrid(x,y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax = axes(projection='3d')
ax.plot_wireframe(X,Y,Z,color='brown')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
title("Wireframe Plot")
show()'''

'''from sympy import *
L = Point(2,6)
M = Point(-2,9)
N = Point(-3,-5)
# Collinearity
print("Collinear =", Point.is_collinear(L,M,N))
# Distances
print("LM =", L.distance(M))
print("MN =", M.distance(N))
print("LN =", L.distance(N))
# Slope LM
line = Line(L,M)
print("Slope LM =", line.slope)'''

'''from sympy import *
P = RegularPolygon(Point(0,0),6,6)
print("Area =", P.area)
print("Perimeter =", P.perimeter)
# Translation in x by 8
P1 = P.translate(8,0)
print("Translated Polygon =", P1)'''

#Q2
'''from matplotlib.pyplot import *
from sympy import *
from math import *
A = Point(-2,5)
B = Point(-2,9)
C = Point(3,5)
D = Point(4,2)
# Original
x = [A.x,B.x,C.x,D.x,A.x]
y = [A.y,B.y,C.y,D.y,A.y]
plot(x,y,color='blue',label='Original')
# a) Translation (2,-5)
T1 = Matrix([[1,0,2],[0,1,-5],[0,0,1]])
# b) Rotation 60°
T2 = Matrix([[cos(pi/3),-sin(pi/3),0],
             [sin(pi/3), cos(pi/3),0],
             [0,0,1]])
# c) Shear (x = x + 5y)
T3 = Matrix([[1,5,0],[0,1,0],[0,0,1]])
# Translation
A1 = A.transform(T1)
B1 = B.transform(T1)
C1 = C.transform(T1)
D1 = D.transform(T1)
plot([A1.x,B1.x,C1.x,D1.x,A1.x],
     [A1.y,B1.y,C1.y,D1.y,A1.y],
     color='red',label='Translation')
# Rotation
A2 = A.transform(T2)
B2 = B.transform(T2)
C2 = C.transform(T2)
D2 = D.transform(T2)
plot([A2.x,B2.x,C2.x,D2.x,A2.x],
     [A2.y,B2.y,C2.y,D2.y,A2.y],
     color='green',label='Rotation')
# Shear
A3 = A.transform(T3)
B3 = B.transform(T3)
C3 = C.transform(T3)
D3 = D.transform(T3)
plot([A3.x,B3.x,C3.x,D3.x,A3.x],
     [A3.y,B3.y,C3.y,D3.y,A3.y],
     color='orange',label='Shear')
axhline(0,color='black')
axvline(0,color='black')
legend()
grid()
show()'''

'''from matplotlib.pyplot import *
from math import *
r = 9
n = 100
theta = 2*pi/n
x = r
y = 0
for i in range(n):
    plot(x,y,'.',color='blue')
    
    x_new = x*cos(theta) - y*sin(theta)
    y_new = x*sin(theta) + y*cos(theta)
    
    x = x_new
    y = y_new
xlabel("X-axis")
ylabel("Y-axis")
axis('equal')
grid()
show()'''