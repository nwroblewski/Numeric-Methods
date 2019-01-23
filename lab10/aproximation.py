#!/usr/bin/env python
# - *- coding: utf- 8 - *-

# Mikołaj Wróblewski AGH UST 3rd year, Computer Science
# Numeric Methods


import numpy as np
import math
import matplotlib.pyplot as plt



def f1(x):
    return 10 + x**2 * 0.5 - 10*np.cos(2*x)

def f2(x):
    return -x * math.sin(math.sqrt(3*abs(x-1)))


def poly_approximation(n,f,x0,x1,d):
    nodes = np.linspace(x0,x1,n)
    values = list(map(f,nodes))
    w = np.random.rand(d)
    matrix = np.zeros((n,d))
    for i in range(n):
        for j in range(d):
            matrix[i,j] = nodes[i] ** j
    w = np.linalg.solve(np.matmul(np.transpose(matrix), matrix) ,np.matmul(np.transpose(matrix), values)) 
    return w,d

def poly_approximation_value(x, w, d):
    p = np.zeros(d)
    for i in range(d):
        p[i] = x ** i
    return np.matmul(p,w)


def tri_approximation(n,f,x0,x1,d):
    nodes = np.linspace(x0,x1,n)
    values = list(map(f,nodes))
    w = np.random.rand(d)
    matrix = np.zeros((n,d))
    for i in range(n):
        for j in range(d):
            matrix[i,j] = np.cos(nodes[i] * j)
    w = np.linalg.solve(np.matmul(np.transpose(matrix), matrix) ,np.matmul(np.transpose(matrix), values)) 
    return w,d

def tri_approximation_value(x,w,d):
    p = np.zeros(d)
    for i in range(d):
        p[i] = np.cos(x * i)
    return np.matmul(p,w)

def test_poly(n, f, x0, x1, d, filename):
    w,d = poly_approximation(n,f,x0,x1,d)
    points = np.linspace(x0,x1,1000)    

    values = list(map(f,points))
    aprox = [poly_approximation_value(x,w,d) for x in points]
    
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Polynomial Approximation')
    plt.plot(points, values, 'b-')
    plt.plot(points,aprox, 'g-')
    #plt.plot(nodes,list(map(f,nodes)), 'y.')
    plt.savefig("./"+filename)

def test_tri(n, f , x0, x1, d, filename):
    w,d = tri_approximation(n,f,x0,x1,d)
    points = np.linspace(x0,x1,1000)

    values = list(map(f,points))
    aprox = [tri_approximation_value(x,w,d) for x in points]

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Trigonometric Approximation')
    plt.plot(points, values, 'b-')
    plt.plot(points,aprox, 'g-')
    #plt.plot(nodes,list(map(f,nodes)), 'y.')
    plt.savefig("./"+filename)

def main():
    #test_poly(20,f1,-2 * np.pi, 2 * np.pi ,5 ,"f1_test_1")
    #test_poly(20,f1,-2 * np.pi, 2 * np.pi ,16 ,"f1_test_2")
    #test_poly(100,f1,-2 * np.pi, 2 * np.pi ,5 ,"f1_test_3")
    #test_poly(100,f1,-2 * np.pi, 2 * np.pi ,16 ,"f1_test_4")
    
    #test_poly(20,f2,-100,100,5,'f2_test_1')
    #test_poly(20,f2,-100,100,16,'f2_test_2')
    #test_poly(100,f2,-100,100,5,'f2_test_3')
    #test_poly(100,f2,-100,100,16,'f2_test_4')
    
    #test_tri(20,f1,-2 * np.pi, 2 * np.pi, 5, "f1_test_1_tri")
    #test_tri(20,f1,-2 * np.pi, 2 * np.pi, 10, "f1_test_2_tri")
    #test_tri(100,f1,-2 * np.pi, 2 * np.pi, 5, "f1_test_3_tri")
    #test_tri(100,f1,-2 * np.pi, 2 * np.pi, 10, "f1_test_4_tri")
    
    #test_tri(20,f2,-100, 100, 4, "f2_test_1_tri")
    #test_tri(20,f2,-100, 100, 11, "f2_test_2_tri")
    #test_tri(100,f2,-100, 100, 4, "f2_test_3_tri")
    test_tri(1000,f2,-100, 100, 8, "f2_test_4_tri")
            
    

if __name__ == "__main__":
    main()
