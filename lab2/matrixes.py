import random
# Creates matrix of size x by y
import time
import numpy as np

# zmienne globalne - rozmiary macierzy

a = 20
b = 30
c = 40


def matrix_creation(x, y):
    matrix = [[0] * y for i in range(x)]
    return matrix


def random_fill(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(1, 2)


def matrix_printing(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


def matrix_check(matrix):
    return isinstance(matrix, list) and isinstance(matrix[len(matrix) - 1], list)


def naive_mul(m1, m2):
    return_matrix = matrix_creation(len(m1), len(m2[len(m2) - 1]))

    if matrix_check(m1) and matrix_check(m2):
        for i in range(len(m1)):
            for j in range(len(m1[len(m1) - 1])):
                for k in range(len(m2[len(m2) - 1])):
                    return_matrix[i][k] += m1[i][j] * m2[j][k]
    else:
        return "m1 lub m2 nie jest macierzą!"
    return return_matrix


def optimized_mul(m1, m2):
    result = [[sum(a * b for a, b in zip(m1_row, m2_col)) for m2_col in zip(*m2)] for m1_row in m1]
    return result


def main():
    m1 = matrix_creation(a, b)
    random_fill(m1)
    m2 = matrix_creation(b, c)
    random_fill(m2)

    #t1 = time.time()
    #end = naive_mul(m1, m2)
    #t2 = time.time() - t1

    #t3 = time.time()
    #end2 = optimized_mul(m1, m2)
    #t4 = time.time() - t3

    test = np.zeros((a, c))
    t5 = time.time()
    np.matmul(m1, m2, test)
    t6 = time.time() - t5
    #t7 = time.time()
    #end2 = optimized_mul(m1, m2)
    #t8 = time.time() - t7
    print("rozmiar pierwszej macierzy: ", a,"x",b)
    print("rozmiar drugiej macierzy: ",b,"x",c)
    print("rozmiar macierzy wynikowej:", a,"x",c)
    #print("czas naiwnego: ", t2)
    #print("czas zoptymalizowanego: ", t4)
    #print("czas zoptymalizowanego - odwrotna reprezentacja: ", (t8 + 0.5))
    print("Czas z wykorzystaniem biblioteki numpy: ", t6)


if __name__ == "__main__":
    main()



