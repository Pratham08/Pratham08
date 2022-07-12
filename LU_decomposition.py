#numpy library implements operations on arrays computationally faster then normal python arrays beacuse of backend fortran execution, hence used 
import numpy as np

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
    print('----------------------------------------------------------')
    print('Lower triangular matrix: ')
    print(L)
    print('----------------------------------------------------------')
    print('Upper triangular matrix: ')
    print(U)
    print('----------------------------------------------------------')
    print('Verification: ')
    print(L@U)
    print('----------------------------------------------------------')
    return L,U

def LU_solver(L,U,fname):
    rows,cols = np.shape(L)
    #load solution vector from the specified text file
    B = np.loadtxt(fname,delimiter=', ')
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
    print('Solution for vector ',end='')
    print(np.transpose(B),end='')
    print(' is:')
    print(X)
    print('----------------------------------------------------------',end='')
    print(L@U@X)
   
#if the current script is implemented then the following condition will return True
#if this python script is imported in some other python script then the following codintion will return False   
if __name__ == '__main__':
    #load coefficient matrix from the specified text file
    A = np.loadtxt('coeff1.txt',delimiter=', ')
    L,U = LU_decomposition(A) #returns L, U
    LU_solver(L,U,'sol.txt') 