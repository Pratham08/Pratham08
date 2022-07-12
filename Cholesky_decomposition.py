#numpy library implements operations on arrays computationally faster then normal python arrays beacuse of backend fortran execution, hence used 
import numpy as np
import math

def cholesky_decomp(M):
    rows, cols = np.shape(M)
    L = np.zeros(np.shape(M)) #define a Lower triangular matrix
    Lt = np.zeros(np.shape(M)) #define L transpose 
    #Cholesky decomposition
    for i in range(0,rows):
        for j in range(0,cols):
            if i==j:
                temp = M[i][i]
                for k in range(0,j):
                    temp -= L[j][k]**2
                temp = math.sqrt(temp)
                L[i][i] = temp
                Lt[i][i] = temp
            elif i>j:
                temp = M[i][j]
                for k in range(0,j):
                    temp -= L[i][k]*L[j][k]
                temp *= 1/L[j][j]
                L[i][j] = temp
                Lt[j][i] = temp
    #print lower triangular matrix and its transpose 
    print('-----------------------------------------------------------')
    print('Lower triangluar matrix is: ')
    print(L)
    print('-----------------------------------------------------------')
    print('Verification: ')
    print(L@Lt)
    if (L@Lt).all() == M.all():
        print('**Lower triangular matrix is correct!**')
    print('-----------------------------------------------------------')
    return L,Lt
    
def LU_solver(L,U,fname):
    rows,cols = np.shape(L)
    #Load the solution vector from the specified text file
    B = np.loadtxt(fname,delimiter=', ')
    Y = np.zeros((rows,1))
    
    #forward substitution
    Y[0] = B[0]/L[0][0]
    for i in range(1,rows):
        Y[i] += B[i]
        for j in range(0,i):
            Y[i] -= Y[j]*L[i][j]
        Y[i] *= 1/L[i][i]
    X = np.zeros((rows,1))
    
    #back substitution
    X[rows-1] = Y[rows-1]/U[rows-1][cols-1]
    for i in range(0,rows-1):
        X[rows-2-i] += Y[rows-2-i]
        for j in range(0,i+1):
            X[rows-2-i] -= X[rows-1-j]*U[rows-2-i][rows-1-j]
        X[rows-2-i] *=  1/U[rows-2-i][rows-2-i]
    #print final solution
    print('Solution for vector ',end='')
    print(np.transpose(B),end='')
    print(' is:')
    print(X)
    print('-----------------------------------------------------------',end='')
  
#if the current script is implemented then the following condition will return True
#if this python script is imported in some other python script then the following codintion will return False    
if __name__ == '__main__':
    #loads coefficient matrix from the specified text file
    M = np.loadtxt('coeff1.txt',delimiter=', ')
    L,U = cholesky_decomp(M) #solves and returns L,U matrix
    LU_solver(L,U,'sol.txt')#forward substitution and back substitution
    