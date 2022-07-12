import numpy as np
import matplotlib.pyplot as plt
import math

#solve by euler method
def Euler_method(V, Xo, h):
    x = [Xo]
    t = [0]
    for i in range(300):
        x_temp = x[i] + V*h
        x.append(x_temp)
        t.append(t[i]+h)
        V += (-x[i]*h)
    plt.plot(t,x)
 
#solve by 4 order runga kutta method  
def RK4_method(Vo, Xo, h):
    x = [Xo]
    t = [0]
    V = [Vo]
    for i in range(300):
        k1x = V[i]
        k1v = -x[i]
        k2x = V[i] + k1v*0.5*h
        k2v = -(x[i] + k1x*0.5*h)
        k3x = V[i] + k2v*h*0.5
        k3v = -(x[i] + k2x*0.5*h)
        k4x = V[i] + k3v*h
        k4v = -(x[i] + k3x*h)
        x_temp = x[i] + ((k1x+2*k2x+2*k3x+k4x)/6)*h
        x.append(x_temp)
        t.append(t[i]+h)
        V_temp = V[i] + ((k1v+2*k2v+2*k3v+k4v)/6)*h
        V.append(V_temp)
    plt.plot(t,x)

#solution by heuns method
def Heuns_method(Vo,Xo,h):
    x = [Xo]
    t = [0]
    for i in range(300):
        x1 = Vo
        v1 = -x[i]
        x2 = Vo + v1*h
        v2 = -(x[i] + h*x1) 
        x.append(x[i] + h*(x1+x2)*0.5)
        Vo += h*(v1+v2)*0.5
        t.append(t[i]+h)
    plt.plot(t,x)

#solution by midpoint method
def midpoint_method(Vo,Xo,h):
    x = [Xo]
    t = [0]
    for i in range(300):
        x1 = Vo
        v1 = -x[i]
        x2 = Vo + v1*h/2
        v2 = -(x[i] + (h/2)*x1) 
        x.append(x[i] + h*x2)
        Vo += h*v2
        t.append(t[i]+h)
    plt.plot(t,x)

#exact analytically solved solution
def exact_soln(Vo,Xo,h):
    x = [Xo]
    t = [0]
    for i in range(300):
        x_temp = math.cos(t[i])
        x.append(x_temp)
        t.append(t[i]+h)
    plt.plot(t,x)

#if the current script is implemented then following code wil run
if __name__ == '__main__':
    h = 0.1
    Euler_method(0,1,h)
    RK4_method(0,1,h)
    Heuns_method(0,1,h)
    midpoint_method(0,1,h)
    exact_soln(0,1,h)
    plt.legend(['Euler','RK4','Heun\'s','Midpoint','Exact'])
    plt.xlabel('Time (in seconds)')
    plt.ylabel('Displacement (in metres)')
    plt.title(f'x vs t (h = {h})')
    plt.show()