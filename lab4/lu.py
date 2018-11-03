#!/usr/bin/env python
# - *- coding: utf- 8 - *-

import numpy as np

# Mikołaj Wróblewski AGH UST 3rd year, Computer Science
# Numeric Methods


def rand_matrix(dimension):
	return np.random.randint(20,size = dimension)		

# wyznaczenie wektora z
# przy użyciu macierzy dolnej trójkątnej i wektora y
def vector_z(L,y):
    z = np.zeros(L.shape[0])
    sum = 0
    for i in range(L.shape[0]):
        for j in range(0,i):
            sum += L[i][j] * z[j]
        z[i] = (y[i] - sum) / L[i][i]
        sum = 0
    return z

def vector_x(U,z):
    x = np.zeros(U.shape[0])
    sum = 0
    for i in range(U.shape[0] - 1, -1, -1):
        print("i" ,i)
        for j in range(U.shape[0] - 1,i , -1):
            print("j",j)
            sum += U[i][j] * x[j]
        x[i] = (z[i] - sum) / U[i][i]
        sum = 0

    return x

# zdekomponowanie macierzy współczynników 
# do postaci macierzy: L - dolnej, U - górnej
def LU(matrix):
	sum1 = 0 
	sum2 = 0	
	
	l = matrix.shape[0]	
	L = np.zeros(matrix.shape)
	U = np.zeros(matrix.shape)
	
	for i in range (matrix.shape[0]):
		L[i][i] = 1


	for i in range (l):		
		for j in range(i,l):
			for k in range(i):
				sum1+= L[i][k] * U[k][j]
			U[i][j] = matrix[i][j] - sum1
			sum1 = 0
		for j in range(i+1,l):
			for k in range(i):
				sum2+= L[j][k] * U[k][i]
			L[j][i] = 1/U[i][i] * ( matrix[j][i] - sum2 )
			sum2 = 0		
			
	return L,U

def LU_method(A,B):
    c = LU(A)
    z = vector_z(c[0],B)
    print(z)
    x = vector_x(c[1],z)
    return x

def main():

    A = np.array([[5,3,2],[1,2,0],[3,0,4]])
    B = np.array([10,5,-2])
    LU_method(A,B)

	
if __name__ == "__main__":
	main()




