import numpy as np
import matplotlib.pyplot as plt

xl = 8
yl = 6

def f_2_x():

    return (-2)

def f_2_y():

    return (-4)

def func(x,y):
    return (2*x*y + 2*x - x**2 - 2*y**2 +72)

def trunc_error(n):
    return (((-1)*(f_2_y())*(6**3) / (12*n**2))*((-1)*(f_2_x())*(8**3) / (12*n)))

#Integration by trapezoidal method
def trapezoidal_method(n):
    x = np.linspace(0,xl,n+1)
    y = np.linspace(0,yl,n+1)
    y1 = np.zeros(n+1)
    hx = xl/n
    hy = yl/n
    for i in range(n+1):
        sum = func(x[0],y[i])
        for j in range(1,n):
            sum += 2*func(x[j],y[i])
        sum += func(x[n],y[i])
        y1[i] = sum*hx/2
    integration = 0
    sum = y1[0]
    for i in range(1,n):
        sum += 2*y1[i]
    sum += y1[n]
    integration = sum*hy/2
    return integration/(xl*yl)

#integration by simpson 1/3 method
def simpson_method1by3():
    x = np.linspace(0,xl,3)
    y = np.linspace(0,yl,3)
    y1 = np.zeros(3)
    for i in range(3):
        y1[i] = xl*(func(x[0],y[i])+4*func(x[1],y[i])+func(x[2],y[i]))/6
    intg = yl*(y1[0] + 4*y1[1] + y1[2])/6
    return intg/(xl*yl)

#integration by simpson 3/8 method
def simpson_method3by8():
    x = np.linspace(0,xl,4)
    y = np.linspace(0,yl,4)
    y1 = np.zeros(4)
    for i in range(4):
        y1[i] = xl*(func(x[0],y[i])+3*func(x[1],y[i])+3*func(x[2],y[i])+func(x[3],y[i]))/8
    intg = yl*(y1[0] + 3*y1[1] + 3*y1[2] + y1[3])/8
    return intg/(xl*yl)

#Plot of result vs no of steps
def plot_trapezoidal():
    x = np.linspace(2,100,99)
    y = np.zeros(99)
    for i in range(99):
        y[i] = trapezoidal_method(int(x[i]))
    plt.xlabel('No. of steps')
    plt.ylabel('Integration result')
    plt.title('Result vs No. of steps')
    plt.plot(x,y)
    plt.show()

#difference between calulated result vs analytically obtained result
def actual_error(a):

    return (abs(a-2816/48))

if __name__ == '__main__':
    n = 1
    print(f'Solution by trapezoidal method: {trapezoidal_method(n)} Error: {actual_error(trapezoidal_method(n))} trunc error: {trunc_error(n)}')
    print(f'Solution by simpson\'s 1/3 method: {simpson_method1by3()} Error: {actual_error(simpson_method1by3())}')
    print(f'Solution by simpson\'s 3/8 method: {simpson_method3by8()} Error: {actual_error(simpson_method3by8())}')
    plot_trapezoidal()
    