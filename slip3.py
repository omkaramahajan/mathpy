'''from matplotlib.pyplot import *
subjects = ['Mathematics','English','Biology','Physics','Chemistry']
marks = [45,35,85,50,60]
barh(subjects, marks, color='brown')
xlabel("Marks")
ylabel("Subjects")
title("Horizontal Bar Graph")
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-5,5,100)
y = x**3 - 3*x + 2
plot(x,y,color='maroon',marker='>',linestyle='-')
xlabel("x")
ylabel("y")
title("Graph of y = x^3 - 3x + 2")
grid()
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-20,20,100)
y = np.linspace(-20,20,100)
X,Y = np.meshgrid(x,y)
Z = np.sqrt(X**2 + Y**2)
ax = axes(projection='3d')
ax.plot_surface(X,Y,Z,color='red')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
title("Surface Plot")
show()'''

'''from sympy import *
L = Point(-5,0)
M = Point(4,0)
N = Point(9,0)
# Collinearity
print("Collinear =", Point.is_collinear(L,M,N))
# Line through L and N
line = Line(L,N)
print("Slope =", line.slope)
x,y = symbols('x y')
print("Equation =", line.equation())'''

'''from sympy import *
P = RegularPolygon(Point(0,0),2,5)
print("Area =", P.area)
print("Perimeter =", P.perimeter)
print("Centroid =", P.centroid)
# Translation in y by 4
P1 = P.translate(0,4)
print("Translated Polygon =", P1)'''

#Q2
'''from matplotlib.pyplot import *
from sympy import *
from math import *
A = Point(0,0)
B = Point(1,0)
C = Point(1,1)
D = Point(0,1)
# Original
x = [A.x,B.x,C.x,D.x,A.x]
y = [A.y,B.y,C.y,D.y,A.y]
plot(x,y,color='blue',label='Original')
# Combined transformation
# a) Reflection x-axis
T1 = Matrix([[1,0,0],[0,-1,0],[0,0,1]])
# b) Rotation 45°
T2 = Matrix([[cos(pi/4),-sin(pi/4),0],
             [sin(pi/4), cos(pi/4),0],
             [0,0,1]])
# c) Scaling -3
T3 = Matrix([[-3,0,0],[0,-3,0],[0,0,1]])
T = T3*T2*T1
A1 = A.transform(T)
B1 = B.transform(T)
C1 = C.transform(T)
D1 = D.transform(T)
x1 = [A1.x,B1.x,C1.x,D1.x,A1.x]
y1 = [A1.y,B1.y,C1.y,D1.y,A1.y]
plot(x1,y1,color='red',label='Transformed')
axhline(0,color='black')
axvline(0,color='black')
legend()
grid()
show()'''

from matplotlib.pyplot import *
from math import *
a = 3   # since y^2 = 4ax → 4a = 12 → a = 3
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
title("Parabola y^2 = 12x")
grid()
show()