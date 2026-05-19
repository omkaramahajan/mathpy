'''from matplotlib.pyplot import *
import numpy as np
# f(x) = x^2
x1 = np.linspace(-10,10,100)
y1 = x1**2
# g(x) = e^(2x+4)
x2 = np.linspace(1,20,100)
y2 = np.exp(2*x2 + 4)
subplot(1,2,1)
plot(x1,y1)
title("f(x) = x^2")
subplot(1,2,2)
plot(x2,y2)
title("g(x) = e^(2x+4)")
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-10,10,100)
y = x**2 + 5
plot(x,y,color='red',marker='>',linestyle='-')
xlabel("x")
ylabel("y")
title("Graph of y = x^2 + 5")
grid()
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(0,2*np.pi,100)
y = np.linspace(0,2*np.pi,100)
X,Y = np.meshgrid(x,y)
Z = np.sin(X**2 + Y**2)
ax = axes(projection='3d')
ax.plot_wireframe(X,Y,Z,color='brown')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
title("Wireframe Plot")
show()'''

'''from sympy import *
P = RegularPolygon(Point(0,0),4,5)
print("Area =", P.area)
# Scaling (x by 3, y by 2)
P1 = P.scale(3,2)
print("Scaled Polygon =", P1)'''

'''from sympy import *
A = Point(2,2)
B = Point(6,2)
C = Point(6,6)
D = Point(2,6)
poly = Polygon(A,B,C,D)
print("Area =", poly.area)
print("Perimeter =", poly.perimeter)
print("Angles =", poly.angles)'''

#Q2
'''from matplotlib.pyplot import *
from sympy import *
A = Point(1,6)
B = Point(0,8)
C = Point(5,3)
# Original
x = [A.x,B.x,C.x,A.x]
y = [A.y,B.y,C.y,A.y]
plot(x,y,color='blue',label='Original')
# Shear (x = x + 5y)
T1 = Matrix([[1,5,0],[0,1,0],[0,0,1]])
# Reflection y-axis
T2 = Matrix([[-1,0,0],[0,1,0],[0,0,1]])
# Translation (1,4)
T3 = Matrix([[1,0,1],[0,1,4],[0,0,1]])
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
r = 6
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