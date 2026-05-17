'''from matplotlib.pyplot import *
sports = ['Cricket','Football','Badminton','Hockey','Other']
students = [34,50,24,10,82]
pie(students, labels=sports, autopct="%1.1f%%")
title("Pie Chart of Students in Sports")
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-5,5,100)
y = x**2 + 5
plot(x,y,color='green',linestyle='--')
xlabel("x")
ylabel("y")
title("Graph of y = x^2 + 5")
grid()
show()'''

'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-20,20,100)
y = np.linspace(-20,20,100)
X,Y = np.meshgrid(x,y)
Z = X**2 - Y**2
ax = axes(projection='3d')
ax.plot_wireframe(X,Y,Z,color='brown')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
title("Wireframe Plot")
show()'''

'''from sympy import *
P = Point(-4,5)
# a) Scaling in x by 2
P1 = P.scale(2,1)
print("Scaling =", P1)
# b) Reflection through y = x
x,y = symbols('x y')
L = Line(y - x)
P2 = P.reflect(L)
print("Reflection =", P2)
# c) Translation in y by 7
P3 = P.translate(0,7)
print("Translation =", P3)'''

'''from sympy import *
A = Point(3,0)
B = Point(0,4)
C = Point(-3,0)
T = Triangle(A,B,C)
print("Area =", T.area)
print("Perimeter =", T.perimeter)
print("Angles =", T.angles)'''

#Q2
'''from matplotlib.pyplot import *
from sympy import *
from math import *
A = Point(1,1)
B = Point(-5,1)
C = Point(-5,-4)
D = Point(1,-4)
# Original
x = [A.x,B.x,C.x,D.x,A.x]
y = [A.y,B.y,C.y,D.y,A.y]
plot(x,y,color='blue',label='Original')
# Rotation 90°
tr1 = Matrix([[0,-1,0],[1,0,0],[0,0,1]])
A1 = A.transform(tr1)
B1 = B.transform(tr1)
C1 = C.transform(tr1)
D1 = D.transform(tr1)
x1 = [A1.x,B1.x,C1.x,D1.x,A1.x]
y1 = [A1.y,B1.y,C1.y,D1.y,A1.y]
plot(x1,y1,color='red',label='Rotation')
# Shear in x-direction (factor 3)
tr2 = Matrix([[1,3,0],[0,1,0],[0,0,1]])
A2 = A.transform(tr2)
B2 = B.transform(tr2)
C2 = C.transform(tr2)
D2 = D.transform(tr2)
x2 = [A2.x,B2.x,C2.x,D2.x,A2.x]
y2 = [A2.y,B2.y,C2.y,D2.y,A2.y]
plot(x2,y2,color='green',label='Shear')
axhline(0,color='black')
axvline(0,color='black')
legend()
grid()
show()'''

'''from matplotlib.pyplot import *
from math import *
r = 7
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