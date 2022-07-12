import matplotlib.pyplot as plt
import numpy as np
import math

def fresnel_eqns(n1,n2):
    theta = np.linspace(0,math.pi/2,1000)
    cosi = np.cos(theta)
    cost = (1 - (n1*np.sin(theta)/n2)**2)**0.5
    r_p = (n1*cost - n2*cosi)/(n1*cost + n2*cosi)
    plt.plot(theta,r_p)
    r_s = (n1*cosi - n2*cost)/(n1*cosi + n2*cost)
    plt.plot(theta,r_s)
    t_s = 2*n1*cosi/(n1*cosi + n2*cost)
    plt.plot(theta,t_s)
    t_p = 2*n1*cosi/(n1*cost + n2*cosi)
    plt.plot(theta,t_p)
    #brewster angle
    index = np.where((r_p <= 0.002) & (r_p > 0))
    print(f'Brewester\'s angle: {theta[index]}')
    plt.plot(theta[index],r_p[index],'o')
    plt.xlabel('Angle of incidence (in radians)')
    plt.ylabel('Coefficients')
    plt.legend(['r_p', 'r_s', 't_s', 't_p' , 'Brewester\'s angle'])

def main():
    n1 = 1.33
    n2 = 2.77
    fresnel_eqns(n1,n2)
    plt.show()
    
if __name__ == '__main__':
    main()