'''from matplotlib.pyplot import *

subjects = ['Mathematics','English','Biology','Physics','Chemistry']
marks = [68,45,79,56,70]
bar(subjects, marks, color='brown')
xlabel("Subjects")
ylabel("Marks")
title("Bar Graph of Marks")
show()'''


'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-10,10,100)
y = x**3 + 10*x - 5
plot(x,y,color='red',linestyle='--')
xlabel("x")
ylabel("y")
title("Graph of y = x^3 + 10x - 5")
grid()
show()'''


'''from matplotlib.pyplot import *
import numpy as np
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
X,Y = np.meshgrid(x,y)
Z = X**2 + Y**2
ax = axes(projection='3d')
ax.plot_surface(X,Y,Z,color='pink')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
title("Surface Plot")
show()'''


'''from sympy import *
P = Point(7,2)
Q = Point(1,8)
print("Distance =", P.distance(Q))
L = Line(P,Q)
print("Slope =", L.slope)
x,y = symbols('x y')
print("Equation =", L.equation())'''

'''from sympy import *
A = Point(2,2)
B = Point(4,2)
C = Point(3,6)
T = Triangle(A,B,C)
print("Centroid =", T.centroid)
T1 = T.translate(2,0)
print("Translated Triangle =", T1)'''


#Q2
'''from matplotlib.pyplot import *
x = [4,6,6,4,4]
y = [3,3,5,5,3]
x1 = x
y1 = [-i for i in y]
x2 = [-i for i in x]
y2 = y
plot(x,y,color='blue',label='Original')
plot(x1,y1,color='red',label='X-axis reflection')
plot(x2,y2,color='green',label='Y-axis reflection')
axhline(0,color='black')
axvline(0,color='black')
xlabel("X-axis")
ylabel("Y-axis")
legend()
grid()
show()'''

'''from matplotlib.pyplot import *
from math import *
r = 5
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