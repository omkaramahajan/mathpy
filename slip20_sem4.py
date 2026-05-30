#Q1
'''from matplotlib.pyplot import *
subjects=['History','Geography','English','Sociology','Psychology']
students=[168,90,195,95,46]
pie(students,labels=subjects,autopct="%1.1f%%",radius=0.7)
title('Pie Chart of Students')
show()'''

#Q2
'''from matplotlib.pyplot import *
from numpy import *
x=linspace(5,10,100)
y=x**2 + 5*x
plot(x,y,ls=':')
xlabel('x')
ylabel('y')
title('Graph of y = x^2 + 5x')
show()'''

#Q3
'''from sympy import *
from matplotlib.pyplot import *
A=Point(1,1)
B=Point(1,6)
C=Point(6,1)
D=Point(6,6)
plot([A.x,B.x,D.x,C.x,A.x],[A.y,B.y,D.y,C.y,A.y],color='black')
title('Quadrilateral ABCD')
show()'''

#Q4
'''from sympy import *
A=Point(1,1)
B=Point(1,4)
C=Point(4,1)
D=Point(4,4)

# Shearing matrix
T=Matrix([[1,3,0],[7,1,0],[0,0,1]])
A1=A.transform(T)
B1=B.transform(T)
C1=C.transform(T)
D1=D.transform(T)
print("Sheared Points =",A1,B1,C1,D1)'''

#Q5
'''from sympy import *
A=Matrix([-3,5])
B=Matrix([3,3])
T=Matrix([[1,3],[4,1]])
A1=T*A
B1=T*B
mid=(A1+B1)/2
print("Midpoint of transformed line =",mid)'''

#Q2 
'''from matplotlib.pyplot import *
from sympy import *
A=Point(4,4)
B=Point(2,4)
C=Point(4,2)
# Original
plot([A.x,B.x,C.x,A.x],[A.y,B.y,C.y,A.y],color='blue')
# Rotation pi/2
T1=Matrix([[0,-1,0],[1,0,0],[0,0,1]])
A1=A.transform(T1)
B1=B.transform(T1)
C1=C.transform(T1)
# Scaling factor 3
T2=Matrix([[3,0,0],[0,3,0],[0,0,1]])
A2=A1.transform(T2)
B2=B1.transform(T2)
C2=C1.transform(T2)
plot([A2.x,B2.x,C2.x,A2.x],[A2.y,B2.y,C2.y,A2.y],color='red')
axhline(0,color='black')
axvline(0,color='black')
grid()
title('Triangle Transformation')
show()'''


'''from matplotlib.pyplot import *
from math import *
a=8
n=100
xmin=0
xmax=100
delta=(xmax-xmin)/(n-1)
x1=xmin
y1=sqrt(32*x1)
for i in range(n):
    plot(x1,y1,marker='.',color='blue')
    plot(x1,-y1,marker='.',color='blue')
    x2=x1+delta
    y2=sqrt(32*x2)
    x1=x2
    y1=y2
xlabel('x axis')
ylabel('y axis')
title('Parabola y^2 = 32x')
show()'''