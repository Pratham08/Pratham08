import numpy as np
import matplotlib.pyplot as plt

#function generator
def func(x,y):
    return (-2*(x**3))+(12*(x**2)) - (20*x) + 8.5

#returns exact solution
def soln(x):
    return (-0.5*x**4)+(4*x**3)-(10*x**2)+(8.5*x) + 1

#return exact solution
def exact_soln(h,start,stop):
    x = [start]
    y = []
    pos = start
    i = 0
    while pos<=stop:
        y.append(soln(x[i]))
        x.append(x[i]+h)  
        pos += h
        i += 1
    x.pop(len(y))
    return x,y  
#solution by Euler's method
def Euler_method(Xo,Yo,h,start,end):
    x = [Xo]
    y = [Yo]
    i = 0
    pos = start
    while pos<end:
        diff = func(x[i],y[i])
        y_new = y[i] + diff*h
        y.append(y_new)
        x.append(x[i]+h)
        pos += h
        i+=1
    return x,y

#Solution by Heun's method
def Heun_method(Xo,Yo,h,start,end):
    x = [Xo]
    y = [Yo]
    i = 0
    pos = start
    while pos < end:
        diff1 = func(x[i],y[i])
        y_o = y[i] + diff1*h
        diff2 = func(x[i]+h,y_o)
        diff = (diff1+diff2)/2
        y_new = y[i] + diff*h
        y.append(y_new)
        x.append(x[i]+h)
        pos += h
        i += 1
    return x,y

#solution by Midpoint method
def midpoint_method(Xo,Yo,h,start,end):
    x = [Xo]
    y = [Yo]
    i = 0
    pos = start
    while pos < end:
        diff1 = func(x[i],y[i])
        y_h = y[i] + diff1*(h/2)
        diff = func(x[i]+(h/2),y_h)
        y_new = y[i] + diff*h
        y.append(y_new)
        x.append(x[i]+h)
        pos += h
        i += 1
    return x,y

#plot the function
def Euler_soln(h_list):
    for i in range(len(h_list)):
        x,y = Euler_method(0,1,h_list[i],0,4)
        plt.plot(x,y)
    x1,y1 = exact_soln(0.005,0,4)
    plt.plot(x1,y1)
    plt.title('Solution by Euler\'s method')
    legend_list = []
    for i in range(len(h_list)):
        legend_list.append(f'h={h_list[i]}')
    legend_list.append('Exact solution')
    plt.legend(legend_list)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

#plot the function
def Heun_soln(h_list):
    for i in range(len(h_list)):
        x,y = Heun_method(0,1,h_list[i],0,4)
        plt.plot(x,y)
    x1,y1 = exact_soln(0.005,0,4)
    plt.plot(x1,y1)
    plt.title('Solution by Heun\'s method')
    legend_list = []
    for i in range(len(h_list)):
        legend_list.append(f'h={h_list[i]}')
    legend_list.append('Exact solution')
    plt.legend(legend_list)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
 
#plot the function
def midpoint_soln(h_list):
    for i in range(len(h_list)):
        x,y = midpoint_method(0,1,h_list[i],0,4)
        plt.plot(x,y)
    x1,y1 = exact_soln(0.005,0,4)
    plt.plot(x1,y1)
    plt.title('Solution by midpoint method')
    legend_list = []
    for i in range(len(h_list)):
        legend_list.append(f'h={h_list[i]}')
    legend_list.append('Exact solution')
    plt.legend(legend_list)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()    

#compares function from different methods for given step-size
def compare(h):
    x1,y1 = Euler_method(0,1,h,0,4)
    x2,y2 = Heun_method(0,1,h,0,4)
    x3,y3 = midpoint_method(0,1,h,0,4)
    x,y = exact_soln(h,0,4)
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.plot(x3,y3)
    plt.plot(x,y)
    plt.legend([f'Euler\'s method','Heun\'s method','Midpoint method','Exact solution'])
    plt.title(f'Comparison plot for h={h}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

#executes if the current file is run
if __name__ == '__main__':
    h_list = [0.5,0.25,0.1,0.05]
    Euler_soln(h_list)
    Heun_soln(h_list)
    midpoint_soln(h_list)
    #compare(0.05)
    