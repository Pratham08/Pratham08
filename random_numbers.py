import random 
import math
import matplotlib.pyplot as plt
import numpy as np


a = 887
c = 701

'''
r_n = [1]
for i in range(m):
    r_n.append(((a*r_n[i] + c)%m)/(m+1))

print(r_n)

print(len(r_n))

for i in range(int(len(r_n)/2)):
    if r_n[2*i]**2 + r_n[2*i+1]**2 <= 1:
        Nc += 1
        
print(8*Nc/(Nt-1))
'''

def lcg1(Nt):
    Nc = 0
    m = 1000
    r_n = [53]
    for i in range(Nt):
        r_n.append(((a*r_n[i] + c)%m)/(m))
    for i in range(int(len(r_n)-1)):
        if (r_n[i]**2 + r_n[i+1]**2 <= 1):
            Nc += 1
    return (4*Nc/Nt)

def lcg(Nt):
    Nc = 0
    m = Nt
    r_n = [67]
    for i in range(Nt):
        r_n.append((a*r_n[i] + c)%m)
    for i in range(Nt):
        r_n[i] /= m
    a1 = 3079
    c1 = 4096
    r_n1 = [733]
    for i in range(Nt):
        r_n1.append((a1*r_n1[i] + c1)%m)
    for i in range(Nt):
        r_n1[i] /= m
    for i in range(len(r_n1)-1):
        if ((r_n[i]**2 + r_n1[i]**2)**0.5 <= 1):
            Nc += 1
    return (4*Nc/Nt)

def monte_carlo(Nt):
    Nc = 0
    m = Nt
    x = np.random.rand(m)
    #y = np.random.rand(m)
    for i in range(int(len(x)/2)):
        if (x[2*i]**2 + x[2*i + 1]**2 <= 1):
            Nc+=1
    return (8*Nc/Nt)
    
def main():
    t = 999
    n = np.arange(1,t+1,1)
    sol = np.zeros(t)
    avg = 0
    for i in range(t):
        sol[i] = lcg(n[i])
        #sol[i] = monte_carlo(n[i])
        avg += sol[i]
    print(f'Pi : {monte_carlo(1000)}')
    print(f'Avg value of Pi by : {avg/t}')
    plt.plot(n,sol)
    x = np.arange(1,t+1,1)
    y = math.pi*(np.ones((t,1)))
    plt.xlabel('No. of points')
    plt.ylabel('Pi')
    plt.title('Pi vs ')
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    main()
    