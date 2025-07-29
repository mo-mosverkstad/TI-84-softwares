from math import *

x=1
y=4
xTarget=3
h=1

def grad(x, y):
    return sqrt(y)-x
g=grad(x, y)
while x<=xTarget:
    print(x,y,g)
    x+=h
    y+=h*g
    g=grad(x,y)
    
print(x,y)