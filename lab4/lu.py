#!/usr/bin/env python
# - *- coding: utf- 8 - *-

import numpy as np
import time as t
import random
from math import sqrt

# Mikołaj Wróblewski AGH UST 3rd year, Computer Science
# Numeric Methods

# Eliminacja Gaussa z częściowym piwotowaniem - żeby skorzystać z macierz z numpy wywołujemy:
# gauss_w_swaps(macierz_z_numpy.tolist()) i będzie działało poprawnie
def guass_w_swaps(a):
    n = len(a)
    x = [0] * n
    
    # poszukiwanie największego elementu w aktualnej kolumnie
    for i in range(n):
        max_e = abs(a[i][i])
        max_row = i
        for k in range(i+1,n):
            if abs(a[k][i]) > max_e:
                max_e = abs(a[k][i])
                max_row = k

        # zamiana "maksymalnego" wiersza z aktualnym
        a[max_row],a[i] = a[i], a[max_row].copy()

        # wyzerowanie wszystkich wierszy poniżej tego jednego w aktualnej kolumnie
        for k in range(i+1,n):
            c = -a[k][i]/a[i][i]
            for j in range(i,n+1):
                if i==j:
                    a[k][j] = 0
                else:
                    a[k][j] += c * a[i][j]

    # rozwiązanie układu dla macierzy górnej trójkątnej
    for i in range(n-1,-1,-1):
        x[i] = a[i][n]/a[i][i]
        for k in range(i-1, -1, -1):
            a[k][n] -= a[k][i] * x[i]
    return x

def random_matrix(n,left,right):
    matrix = np.zeros((n,n+1))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            matrix[i][j] = random.randint(left, right)
    return matrix


# rozbija macierz z numpy na 2 macierze, macierz b i macierz x będącą ostatnią kolumną macierzy wejściowej
def split_matrix(a):
    x = np.zeros(a.shape[1])
    b = np.zeros((a.shape[0],a.shape[0]))
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if j == a.shape[0]:
                x[i] = a[i][j]
            else:
                b[i][j] = a[i][j]
    return b , x

# wyznaczenie wektora z
# przy użyciu macierzy dolnej trójkątnej i wektora y , L * z = y - forward substitution
def vector_z(L,y):
    z = np.zeros(L.shape[0])
    sum = 0
    for i in range(L.shape[0]):
        for j in range(0,i):
            sum += L[i][j] * z[j]
        z[i] = (y[i] - sum) / L[i][i]
        sum = 0
    return z

# wyznaczenie ostatecznego wyniku 
# przy użyciu wektora 'z' uzyskanego w ramach równania u góry, tu wykonujemy U * x = z - backward substitution
def vector_x(U,z):
    x = np.zeros(U.shape[0])
    sum = 0
    for i in range(U.shape[0] - 1, -1, -1):
        for j in range(U.shape[0] - 1,i , -1):
            sum += U[i][j] * x[j]
        x[i] = (z[i] - sum) / U[i][i]
        sum = 0

    return x

# zdekomponowanie macierzy współczynników do rozkładu Doolitle'a
# do postaci macierzy: L - dolnej, U - górnej
def LU_decomposition_doolitle(matrix):
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
            
            if U[i][i] == 0:
                print("U can't divide by zero, decomposition failed.")
                return None
            L[j][i] = 1/U[i][i] * ( matrix[j][i] - sum2 )
            sum2 = 0		
			
    return L,U


# zdekomponowanie macierzy współczynników do rozkładu Croute'a
# do postaci macierzy: L - dolnej, U - górnej
def LU_decomposition_crout(matrix):
    L = np.zeros(matrix.shape)
    U = np.zeros(matrix.shape)
    l = matrix.shape[0]
    sum1 = 0
    sum2 = 0

    for i in range(matrix.shape[0]):
        U[i][i] = 1
    
    for i in range(l):
        for j in range(i,l):
            for k in range(i):
                sum1+= L[j][k] * U[k][i]
            L[j][i] = matrix[j][i] - sum1
            sum1 = 0

        for j in range(i,l):
            for k in range(i):
                sum2+= L[i][k] * U[k][j]
            U[i][j] = (matrix[i][j] - sum2) / L[i][i]
            sum2 = 0
            
    return L,U

# zdekomponowanie macierzy współczynników do rozkładu Choleskiego
# do postaci macierzy: L - dolnej, U - górnej
def LU_decomposition_cholesky(matrix):
    L = np.zeros(matrix.shape)
    U = np.zeros(matrix.shape) # macierz U w tym przypadku jest po prostu transponowaną macierzą L
    l = matrix.shape[0]
    sum1 = 0

    for i in range(l):
        for j in range(i+1):
            sum1 = sum(L[i][k] * L[j][k] for k in range(j))

            if i==j:
                L[i][j] = sqrt(matrix[i][i] - sum1)
            else:
                L[i][j] = (matrix[i][j] - sum1) / L[j][j]

    # transponowanie macierzy L
    for i in range(l):
        for j in range(l):
            U[i][j] = L[j][i]

    return L,U

# metoda LU z użyciem dekompozycji wskazanej jako fn
# UWAGA - rozkład choleskiego nie zawsze może być zastosowany
def LU(A,B,fn):
    c = fn(A)
    if c==None:
        return None
    z = vector_z(c[0],B) # forward substitution
    x = vector_x(c[1],z) # backward substitution
    return x

def main():
    c = np.array([[2,1,-1,8],
    [-3,-1,2,-11],
    [-2,1,2,-3]])
    A = np.array([[5,3,2],[1,2,0],[3,0,4]])
    A1 = np.array([[4,12,-16],[12,37,-43],[-16,-43,98]]) #for testing cholesky
    B = np.array([10,5,-2])
    print(guass_w_swaps(c.tolist()))
    #tests_basic()
	
if __name__ == "__main__":
	main()




