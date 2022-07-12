import numpy as np
import matplotlib.pyplot as plt
from math import exp

#shooting method with RK4
def shooting_method(h,T0,Tn):
    g1 = 10
    g2 = 20
    x1,T1 = RK4_method(g1,T0,h)
    plt.plot(x1,T1)
    x2,T2 = RK4_method(g2,T0,h)
    plt.plot(x2,T2)
    s = (g2-g1)/(T2[int(10/h) - 1] - T1[int(10/h)-1])
    g = g1 + s*(Tn - T1[int(10/h)-1])
    x3,T3 = RK4_method(g,T0,h)
    plt.plot(x3,T3)

#RK4_method for solving ODE through initial conditions
def RK4_method(Zo, To, h):
    T = [To]
    x = [0]
    z = [Zo]
    n = int(10/h)
    for i in range(n):
        k1x = z[i]
        k1v = 0.01*(T[i] - 20)
        k2x = z[i] + k1v*0.5*h
        k2v = 0.01*(T[i] + k1x*0.5*h - 20)
        k3x = z[i] + k2v*h*0.5
        k3v = 0.01*(T[i] + k2x*0.5*h - 20)
        k4x = z[i] + k3v*h
        k4v = 0.01*(T[i] + k3x*h - 20)
        T_temp = T[i] + ((k1x+2*k2x+2*k3x+k4x)/6)*h
        T.append(T_temp)
        x.append(x[i]+h)
        z_temp = z[i] + ((k1v+2*k2v+2*k3v+k4v)/6)*h
        z.append(z_temp)
    return x,T

#finite difference method function with stepsize and boundary conditions as parameters
def finite_diff_method(h,T0,Tn):
    n = int((10/h)-2)
    A = (2 + 0.01*(h**2))*np.eye(n)
    for i in range(0,n-1):
        A[i][i+1] = -1
    for i in range(1,n):
        A[i][i-1] = -1
    B = 0.01*(h**2)*20*np.ones((n,1))
    x = np.linspace(0,10,int(10/h))
    B[0] += T0
    B[n-1] += Tn
    return A,B,x

# LU decomposition
def LU_decomposition(A):
    rows, cols = np.shape(A)
    #check for square matrix condition
    if rows!=cols:
        raise Exception('Input coefficient matrix should be square matrix')
    L = np.identity(rows) #defining the lower triangular matrix
    U = np.zeros((rows,cols)) #defining the upper triangular matrix
    U = A 
    for i in range(0,rows): 
        for j in range(i+1,rows):
            temp = U[j][i]/U[i][i]
            U[j] = U[j] - temp*U[i]
            L[j][i] = temp
    return L,U

def LU_solver(L,U,B):
    rows,cols = np.shape(L)
    #load solution vector from the specified text file
    Y = np.zeros((rows,1))
    
    #forward substitution
    Y[0] = B[0]/L[0][0]
    for i in range(1,rows):
        Y[i] += B[i]
        for j in range(0,i):
            Y[i] -= Y[j]*L[i][j]
    X = np.zeros((rows,1))
    
    #back substitution
    X[rows-1] = Y[rows-1]/U[rows-1][cols-1]
    for i in range(0,rows-1):
        X[rows-2-i] += Y[rows-2-i]
        for j in range(0,i+1):
            X[rows-2-i] -= X[rows-1-j]*U[rows-2-i][rows-1-j]
        X[rows-2-i] *=  1/U[rows-2-i][rows-2-i]
    return X

#exact analytical solution solved using calculus rules
def analytical_soln(h):
    n = int(10/h)
    T = np.zeros((n,1))
    x = np.linspace(0,10,n)
    for i in range(n):
        T[i] = 73.4523*exp(0.1*x[i]) - 53.4523*exp(-0.1*x[i]) + 20
    plt.plot(x,T)

#if current script is run then the following code will be executed
if __name__ == '__main__':
    h = 0.1
    shooting_method(h,40,200)
    A,B,x = finite_diff_method(h,40,200)   
    #print(A)
    L,U = LU_decomposition(A)
    T = LU_solver(L,U,B)
    #print(X)
    a1 = [40,200]
    T1 = np.zeros((len(T)+2,1))
    T1[0] = a1[0]
    T1[len(T)+1] = a1[1]
    for i in range(1,len(T)+1):
        T1[i] = T[i-1]
    plt.plot(x,T1)
    analytical_soln(h)
    plt.legend(['z = 10','z = 20','Shooting (exact)','Finite difference','Analytical soln'])
    plt.xlabel('x (in  m)')
    plt.ylabel('T (in degrees celsius)')
    plt.title(f'T vs x (h = {h})')
    plt.show()
    #print(np.shape(X))