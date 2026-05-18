'''from matplotlib.pyplot import *
import numpy as np
# f(x) = x^3
x1 = np.linspace(-5,5,100)
y1 = x1**3
# g(x) = e^x
x2 = np.linspace(1,10,100)
y2 = np.exp(x2)
subplot(2,1,1)
plot(x1,y1)
title("f(x) = x^3")
subplot(2,1,2)
plot(x2,y2)
title("g(x) = e^x")
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(1,20,100)
y = 2*x + 5
plot(x,y,color='skyblue',linestyle='--')
xlabel("x")
ylabel("y")
title("Graph of y = 2x + 5")
grid()
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(0,2*np.pi,100)
y = np.linspace(0,2*np.pi,100)
X,Y = np.meshgrid(x,y)
Z = np.cos(X**2 + Y**2)
ax = axes(projection='3d')
ax.plot_wireframe(X,Y,Z,color='brown')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
title("Wireframe Plot")
show()'''

'''from sympy import *
A = Point(0,0)
B = Point(1,0)
C = Point(1,1)
D = Point(0,1)
square = Polygon(A,B,C,D)
print("Area =", square.area)
print("Perimeter =", square.perimeter)
print("Centroid =", square.centroid)'''

'''from sympy import *
from math import *
P = Point3D(2,-1,3)
theta = pi/2   # 90 degrees
R = Matrix([[cos(theta), -sin(theta), 0],
            [sin(theta),  cos(theta), 0],
            [0,0,1]])
P1 = P.transform(R)
print("Rotated Point =", P1)'''

#Q2
'''from matplotlib.pyplot import *
from sympy import *
A = Point(-2,7)
B = Point(-5,-1)
C = Point(4,3)
# Original
x = [A.x,B.x,C.x,A.x]
y = [A.y,B.y,C.y,A.y]
plot(x,y,color='blue',label='Original')
# Shearing
T1 = Matrix([[1,3,0],[4,1,0],[0,0,1]])
# Reflection x-axis
T2 = Matrix([[1,0,0],[0,-1,0],[0,0,1]])
# Translation y by 7
T3 = Matrix([[1,0,0],[0,1,7],[0,0,1]])
T = T3*T2*T1
A1 = A.transform(T)
B1 = B.transform(T)
C1 = C.transform(T)

x1 = [A1.x,B1.x,C1.x,A1.x]
y1 = [A1.y,B1.y,C1.y,A1.y]
plot(x1,y1,color='red',label='Transformed')
axhline(0,color='black')
axvline(0,color='black')
legend()
grid()
show()'''

'''from matplotlib.pyplot import *
from math import *
r = 8
n = 75
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