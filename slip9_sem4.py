'''from matplotlib.pyplot import *
import numpy as np
# f(x) = sin(x^2)
x1 = np.linspace(-10,10,100)
y1 = np.sin(x1**2)
# g(x) = cos(x^2)
x2 = np.linspace(0,np.pi,100)
y2 = np.cos(x2**2)
subplot(2,1,1)
plot(x1,y1)
title("f(x) = sin(x^2)")
subplot(2,1,2)
plot(x2,y2)
title("g(x) = cos(x^2)")
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-10,10,100)
y = x**2 + np.exp(2*x + 5)
plot(x,y,color='red',linestyle='-.')
xlabel("x")
ylabel("y")
title("Graph of y = x^2 + e^(2x+5)")
grid()
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-20,20,100)
y = np.linspace(-20,20,100)
X,Y = np.meshgrid(x,y)
Z = X**3 + Y**3
ax = axes(projection='3d')
ax.plot_surface(X,Y,Z,color='pink')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
title("Surface Plot")
show()'''

'''from sympy import *
A = Point(0,0)
B = Point(1,0)
C = Point(1,1)
D = Point(0,1)
square = Polygon(A,B,C,D)
print("Area =", square.area)
print("Perimeter =", square.perimeter)
print("Centroid =", square.centroid)
print("Angles =", square.angles)'''

'''from sympy import *
A = Point3D(2,3,5)
B = Point3D(-4,7,9)
# Reflection through XZ-plane (y -> -y)
A1 = Point3D(A.x,-A.y,A.z)
B1 = Point3D(B.x,-B.y,B.z)
print("Reflected A =", A1)
print("Reflected B =", B1)'''

#Q2
'''from matplotlib.pyplot import *
from sympy import *
A = Point(4,4)
B = Point(-4,4)
C = Point(-4,-4)
D = Point(4,-4)
# Original
x = [A.x,B.x,C.x,D.x,A.x]
y = [A.y,B.y,C.y,D.y,A.y]
plot(x,y,color='blue',label='Original')
# a) Shear in y (y = y - 3x)
T1 = Matrix([[1,0,0],[-3,1,0],[0,0,1]])
# b) Reflection x-axis
T2 = Matrix([[1,0,0],[0,-1,0],[0,0,1]])
# c) Translation (5,8)
T3 = Matrix([[1,0,5],[0,1,8],[0,0,1]])
T = T3*T2*T1
A1 = A.transform(T)
B1 = B.transform(T)
C1 = C.transform(T)
D1 = D.transform(T)
plot([A1.x,B1.x,C1.x,D1.x,A1.x],
     [A1.y,B1.y,C1.y,D1.y,A1.y],
     color='red',label='Transformed')
axhline(0,color='black')
axvline(0,color='black')
legend()
grid()
show()'''

'''from matplotlib.pyplot import *
from math import *
a = 9   # since y^2 = 4ax → 4a = 36 → a = 9
n = 75
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
title("Parabola y^2 = 36x")
grid()
show()'''