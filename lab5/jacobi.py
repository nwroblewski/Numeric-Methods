#!/usr/bin/env python
# - *- coding: utf- 8 - *-
import functools as fun
import numpy as np

# Mikołaj Wróblewski AGH UST 3rd year, Computer Science
# Numeric Methods


#Laplasian matrix of size n by n generator
def laplasian_gen(n):
    a = np.zeros((n,n))
    for i in range(n):
            if i == 0:
                a[i][i] = 2
                a[i][i+1] = -1
            if i == n-1:
                a[i][i-1] = -1
                a[i][i] = 2
            if i!=0 and i!=n-1:
                a[i][i-1] = -1
                a[i][i] = 2
                a[i][i+1] = -1 
    return a


def compare_solutions(a,b):
    return fun.reduce(lambda x,y: x and y,(list(map(lambda x,y: epsilon_euqals(x,y),a,b))))

def epsilon_euqals(a,b):
    return abs(a-b) < 1e-9

#function used to generate diagonally dominant matrices of size n by n

def dominant_matrix_gen(n):
    a = np.random.randint(-10,10,(n,n))
    check_sum = 0

    #checking if generated matrix is diagonally dominant
    #if not - make it diagonally dominant by adding sum of all elements in the row to the diagonal element

    for i in range(n):
        for j in range(n):
            if i!=j:
                check_sum += abs(a[i][j])    
        if a[i][i] <= check_sum:
            a[i][i] = check_sum + abs(a[i][i])
        check_sum = 0
    return a


# METODA JACOBIEGO
# a - macierz kwadratowa
# b - macierz współczynników

def jacobi(a,b,n = 1000,x = None):
    norms = []
    if x is None:
        x = np.zeros(a.shape[0])
    
    #wektor elementów diagonalnych
    D = np.diag(a)
    R = a - np.diagflat(D)

    # Checking standard convergence condition
    iteration_matrix = np.matmul(np.linalg.inv(np.diagflat(D)),R)
    spectral = max(np.linalg.eigvals(abs(iteration_matrix)))
    if spectral > 1:
        print(spectral)
        print("Convergence condition wasn't met.")
        return x # at this point we will always be returning guess list or list filled with 0
    
    for i in range(n):
        diff1 = 0
        x_new = np.zeros_like(x)
        
        x_new = (b - np.dot(R,x)) / D
        
        #diffs are only used for plotting rate of convergence
        
        for j in range(x.shape[0]):
            diff1 = diff1 + abs(x_new[j] - x[j])
        norms.append(diff1)
        
        if np.allclose(x, x_new, atol=1e-10, rtol=0.):
            break
        
        # print(x_new - x)
        x = x_new
        
    return x,norms

# METODA GAUSSA-SEIDELA

def gauss_seidel(a,b,n = 1000,x = None):
    if x is None:
        x = np.zeros(a.shape[0])
    norms = []
    
    for i in range(n):
        x_new = np.zeros_like(x)
        diff1 = 0

        for i in range(a.shape[0]):
            s1 = np.dot(a[i, :i], x_new[:i])
            s2 = np.dot(a[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / a[i, i]
        
        #diffs are only used for plotting rate of convergence

        for j in range(x.shape[0]):
            diff1 = diff1 + abs(x_new[j] - x[j])
        
        
        norms.append(diff1)
        
        if np.allclose(x, x_new, atol=1e-10, rtol=0.):
            break
        x = x_new
        
    return x,norms
    


#---------- TESTS FUNCTIONS ------------#

def tests_basic(fn,a):
    n = 20
    outputs = []
    print("Test of",fn)
    for i in range(1):
            print("test",i)
            # a = dominant_matrix_gen(n)
            print(a)
            # a = np.random.randint(-10,10,(n,n))  - swap this line with 
            b = np.random.randint(-5,10,size = 10)
            s = fn(a,b,1000)
            s1 = s[0]
            s2 = np.linalg.solve(a,b).tolist()
            for i in range(len(s[1])):
                print(s[1][i])
            if compare_solutions(s1,s2) == False:
                print("The matrix test failed")
                return None
            outputs += [compare_solutions(s1,s2)]

    if fun.reduce(lambda x,y: x and y,outputs) == True:
        print("Tests passed")

def test_curious():
    a = np.array([[1,2],[2,1]])
    b = np.array([[1,2]])
    jacobi(a,b)

# def test_laplasian():


def main():
    # print("Jacobi tests:")
    # tests_basic(gauss_seidel)
    # print("Gauss tests:")
    # tests_basic(gauss_seidel)
    # test_curious()
    # print(laplasian_gen(5))
    # print(laplasian_gen(10))
    # array = np.loadtxt("laplasian.txt",delimiter='.')
    # print(array)
    c = laplasian_gen(10)
    tests_basic(gauss_seidel,c)

if __name__ == "__main__":
    main()
