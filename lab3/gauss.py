#!/usr/bin/env python
import numpy as np 
import random
import time
from functools import reduce

# Mikołaj Wróblewski AGH UST 3rd year, Computer Science
# Numerical Methods

# Utilities functions

# funkcja używana do porównywania dwóch wartości
# z dokładnością do 1e-10

def epsilon_euqals(a,b):
    return abs(a-b) < 1e-10

# funkcja używana do porówywania list wynikowych
# !IMPORTANT - trzeba pamiętać by wynik uzyskany przez bibliotekę przekazywać jako
# wynik.tolist() z uwagi na lekko inną reprezentację macierzy aniżeli w "czystym" pythonie
# a , b - listy wynikowe
# zwraca true, jeżeli porównanie odpowiadających sobie indeksów jest równe z dokładnością
# do stałego epsilon

def compare_solutions(a,b):
    return reduce(lambda x,y: x and y,(list(map(lambda x,y: epsilon_euqals(x,y),a,b))))

# tworzenie macierzy o rozmiarze x na y przy użyciu czystego pythona

def matrix_creation(x, y):
    matrix = [[0] * y for i in range(x)]
    return matrix

# wypełnianie przekazanej macierzy losowymi liczbami całkowitymi
# z zakresu <left,right>

def random_fill(matrix,left,right):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(left, right)


# rozbija macierz na macierz kwadratową b i kolumnę wyrazów wolnych x, w celu 
# testowania na funkcji bibliotecznej
# x - kolumna wyrazów wolnych w postaci listy
# b - macierz n na n
# funkcja zwraca krotkę (b,x)

def split_matrix(a):
    x = [0] * len(a)
    b = [[0] * len(a) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[len(a) - 1])):
            if j == len(a):
                x[i] = a[i][j]
            else:
                b[i][j] = a[i][j]
    return b , x


# Eliminacja Gaussa - metoda naiwna
# a - macierz rozmiaru n na n + 1 (ostatnia kolumna to kolumna wyrazów wolnych)

def gauss(a):
    n = len(a)
    x = [0] * n
    for j in range(n):
        for i in range(j+1, n):
            c = a[i][j] / a[j][j]
            for k in range(n+1):
                a[i][k] -= c * a[j][k]
    x[n-1] = a[n-1][n] / a[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += a[i][j]*x[j]
        x[i] = (a[i][n] - sum) / a[i][i]
    return x


# Eliminacja Gaussa z częściowym piwotowaniem
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

# proste testy na losowo generowanych macierzach

def tests_basic(fn):
    n = 10
    outputs = []
    for i in range(30):
            a = matrix_creation(n,n+1)
            random_fill(a,1,20)
            b = split_matrix(a)
            try:
                s1 = fn(a)
            except ZeroDivisionError:
                print("Attempted to divide by zero, aborting...")
                return None

            s2 = np.linalg.solve(b[0],b[1]).tolist()
            if compare_solutions(s1,s2) == False:
                print("The matrix test failed")
                return None

            outputs += [compare_solutions(s1,s2)]

    if reduce(lambda x,y: x and y,outputs) == True:
        print("Tests passed with usage of" , fn)


def tests_curious():
    #1st test case - just a basic one
    a = [[2,1,-1,8],
    [-3,-1,2,-11],
    [-2,1,2,-3]]
    a_1 = np.array([[2,1,-1],[-3,-1,2],[-2,1,2]])
    b_1 = np.array([8,-11,-3])
    solution_1 = np.linalg.solve(a_1,b_1).tolist()
    solution_2 = gauss(a)
    print("Test1 passed: ", compare_solutions(solution_1,solution_2))

    #2nd test case - tutaj bazowa implementacja powinna się "wykrzaczyć"
    #metoda z pivotem powinna wykonać się poprawnie

    a1 = [[0,4,-2,-10],
    [4,8,6,20],
    [6,-4,2,18]]

    a1_1 = np.array([[0,4,-2],[4,8,6],[6,-4,2]])
    b1_1 = np.array([-10,20,18])

    solution1_1 = np.linalg.solve(a1_1,b1_1).tolist()
    try:
        solution1_2 = gauss(a1)
    except ZeroDivisionError:
        print("Attempted to divide by zero")
    solution1_3 = guass_w_swaps(a1)

    print("Test2 passed: ", compare_solutions(solution1_3,solution1_1))


    # 3rd test case - duże wartości numeryczne - najprostsze częściowe piwotowanie
    # może dać wyniki rozmijające się z prawdą
    c = 5e20
    a2 = [[2,2*c,2*c],
    [1,1,2]]
    b = split_matrix(a2)
    solution2_1 = guass_w_swaps(a2)
    solution2_2 = np.linalg.solve(b[0],b[1])
    print("Gauss with pivoting: ",solution2_1)
    print("Gauss with library: ",solution2_2)

    
def performance_tests_pivoting():
    n = 2
    for i in range(2,11):
        a = matrix_creation(n ** i, (n**i) +1)
        random_fill(a,1,20)
        t5 = time.time()
        guass_w_swaps(a)
        t6 = time.time() - t5
        print(n ** i,",",round(t6,10))

def performance_tests_lib():
    n = 2
    for i in range(2,11):
        a = matrix_creation(n ** i, (n**i) +1)
        random_fill(a,1,20)
        b = split_matrix(a)
        t5 = time.time()
        np.linalg.solve(b[0],b[1])
        t6 = time.time() - t5
        print(n ** i,",", round(t6,10))

def main():
    tests_curious()

if __name__ == "__main__":
    main()