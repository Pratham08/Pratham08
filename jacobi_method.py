import numpy as np
import math

#warnings.filterwarnings('ignore')        
def trunc(a,n):
    temp = a*(10**n)
    temp = math.trunc(temp)
    a = round(temp/(10**n),n)
    return a

def eigensolver_jacobi(x):
    x = x.astype('float64')
    rows,cols = np.shape(x)
    for i in range(50):
        for p in range(0,rows):
            for q in range(0,p):
                if p!=q:
                    if abs(x[p][q]) >= 0.00001:
                        #print(p,q)
                        theta = (x[q][q] - x[p][p])/(2*x[p][q])
                        #theta = round(theta,10)
                        if theta>0:
                            t = (1/(theta + (theta**2 + 1)**0.5))
                        else:
                            t = (-1/(-theta + (theta**2 + 1)**0.5))
                        c = 1/((t**2 + 1)**0.5)
                        s = c*t
                        d = np.copy(x)
                        d[p][q] = 0
                        d[q][p] = 0
                        d[p][p] = (c**2)*x[p][p] + (s**2)*x[q][q] - 2*c*s*x[p][q]
                        d[q][q] = (s**2)*x[p][p] + (c**2)*x[q][q] + 2*c*s*x[p][q]
                        for j in range(0,rows):
                            if j!=p and j!=q:
                               d[j][p] = c*x[j][p] - s*x[j][q]
                               d[p][j] = np.copy(d[j][p])
                               d[j][q] = c*x[j][q] + s*x[j][p]
                               d[q][j] = np.copy(d[j][q])
                        x = np.copy(d)
        #print(i)
    print('Eigenvalues: ')
    eigen = []
    for i in range(rows):
        eigen.append(x[i][i])
    eigen.sort()
    for i in range(rows-1):
        print(f'{round(eigen[rows-1-i],5)}, ',end='')
    print(round(eigen[0],5))
                    
def build_matrix():
    rows = 10
    temp1 = 4*(np.identity(rows))
    temp2 = np.zeros((rows,rows))
    j = 1
    for i in range(0,rows-1):
        temp2[i][j] = 2
        j+=1
    temp3 = np.zeros((rows,rows))
    k = 2
    for i in range(0,rows-2):
        temp3[i][k] = 1
        k+=1
    M = temp1+temp2+temp3+np.transpose(temp2) + np.transpose(temp3)
    return M

if __name__ == '__main__':
    x = np.loadtxt('jacobiQ_matrix.txt',delimiter=', ')
    eigensolver_jacobi(x)
    M = build_matrix()
    eigensolver_jacobi(M)
                    