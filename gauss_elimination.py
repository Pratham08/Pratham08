#numpy library implements operations on arrays computationally faster then normal python arrays beacuse of backend fortran execution, hence used 
import numpy as np

#returns solution(1D array) of the linear equation when augmented matrix is passed as a parameter
def gauss_elimn(M):
    rows, cols = np.shape(M)
    
    #gauss elimination
    for i in range(0,rows):
        #partial pivoting 
        #the greatest element below the pivot element in the same column is found 
        
        greatest_index = i
        for k in range(i+1,rows):
            if abs(M[k][i]) > abs(M[greatest_index][i]):
                greatest_index = k
        #if the greatest element found is not equal to the piviot element then the rows are swapped
        if greatest_index != i:
            temp1 = np.copy(M[i])
            M[i] = np.copy(M[greatest_index])
            M[greatest_index] = np.copy(temp1)
        #error check to find if the pivot element is zero
        if abs(M[i][i]) == 0.0:
            raise Exception('No unique solution!')
        
        #gauss elimination is performed to convert all the elements below it in same column to zero
        for j in range(i+1,rows):
            temp = M[j][i]/M[i][i]
            M[j] = M[j] - temp*M[i]
        #print(M)
    #print(M)
    x1 = np.zeros((rows,1))

    #back substitution
    x1[rows-1] = M[rows-1][cols-1]/M[rows-1][cols-2]
    for i in range(0,rows-1):
        x1[rows-2-i] += M[rows-2-i][cols-1]
        for j in range(0,i+1):
            x1[rows-2-i] -= x1[rows-1-j]*M[rows-2-i][cols-2-j]
        x1[rows-2-i] *= 1/M[rows-2-i][rows-2-i]
    #print(x1+'\n')
    #back substitution
    for k in range(3,8):
        x = np.zeros((rows,1))
        x[rows-1] = np.round(M[rows-1][cols-1]/M[rows-1][cols-2],k)
        for i in range(0,rows-1):
            x[rows-2-i] += M[rows-2-i][cols-1]
            for j in range(0,i+1):
                x[rows-2-i] -= x[rows-1-j]*M[rows-2-i][cols-2-j]
            x[rows-2-i] *= 1/M[rows-2-i][rows-2-i]
        print('Solution: ',end='')
        print(x)
        print('relative error: ',end='')
        print((x1-x)*100/x1)
        print('--------------------------------------------------')
    

#if the current script is implemented then the following condition will return True
#if this python script is imported in some other python script then the following codintion will return False
if __name__ == '__main__':
    #Loads augmented matrix from the specified text file from same directory as the current python file
    M = np.loadtxt('matrix2.txt',delimiter=', ')
    M = np.round(M,6)
    #prints the final solution
    gauss_elimn(M)