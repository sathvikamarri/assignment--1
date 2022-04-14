import matplotlib.pyplot as plt
import numpy as np
from numpy import *

#generating the triangle
R=5
ang_P=np.pi/3
Q = np.array([0,0])
P = np.array([5,0])
R = np.array([5,-8])
S = np.array([2,-3.2])
T = np.array([3,0])

#annotating the points
x=[0,5,5,2,3]
y=[0,-8,0,-3.2,0]
text = ["Q", "P", "R", "S", "T"]
plt.text(P[0],P[1], "Q", color='red')
plt.text(Q[0],Q[1], "P", color='red')
plt.text(R[0],R[1], "R", color='red')
plt.text(S[0],S[1], "S", color='red')
plt.text(T[0],T[1], "T", color='red')

#plotting scatter plot
plt.scatter(x,y)
plt.plot(x,y,marker='o',color='none')

#drawing the lines
x1=(0,5)
y1=(0,0)
plt.plot(x1,y1,color='black')
x2 = [0,5]
y2 = [0,-8]
plt.plot(x2,y2,color='black')
x3 = [3,2]
y3 = [0,-3.2]
plt.plot(x3,y3,color='black')
x4 = [5,5]
y4 = [-8,0]
plt.plot(x4,y4,color='black')

plt.grid()
plt.show()
