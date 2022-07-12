import numpy as np
import time

def time_complexity(function):
    def wrapper(*args,**kwargs):
        starttime = time.time()
        result = function(*args,**kwargs)
        endtime = time.time()
        print(function.__name__ + ' implemented in '+ str((endtime-starttime)*1000))
        return result
    return wrapper

@time_complexity
def gauss_jordan_elimn(M):
    rows, cols = np.shape(M)
                    
    #gauss jordan elimination
    for i in range(0,rows):
        #partial pivoting
        if abs(M[i][i]) < 1:
            for j in range(i+1,rows):
                if abs(M[i][i]) < abs(M[j][i]):
                    #swaping all the elements of a row with another row
                    temp = np.copy(M[i])
                    M[i] = M[j]
                    M[j] = temp
        #pivoting ends
        for j in range(0,rows):
            if i!=j:
                temp = M[j][i]/M[i][i]
                M[j] = M[j] - temp*M[i]
        
    #print(M)        
    #create solution matrix and initialize to zero
    x = np.zeros((rows,1))
    
    #re-substitution
    for i in range(0,rows):
        x[i] = M[i][cols-1]/M[i][i] 
    
    return np.transpose(x)


if __name__ == '__main__':
    #Loads augmented matrix from the specified text file from same directory as the current python file
    M = np.loadtxt('matrix1.txt',delimiter=', ') 
    
    #Print the final solution
    print(gauss_jordan_elimn(M))