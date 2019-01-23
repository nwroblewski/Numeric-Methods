#!/usr/bin/env python
# - *- coding: utf- 8 - *-

import numpy as np
import random
import math

# range 0 to 2 
def lin(x):
    return x

# range 1 to 2 (max at 1, min at 2)
def f1(x):
    return 1/x**2

# range 1 to 6 (max at 1, min at 6)
def f2(x):
    return 1/math.sqrt(x**5 + 8)

# range 1 to 22 (max at 1, min at 22)
def f3(x):
    return 1/math.sqrt(x+8)

# range 1 to 22 (max val at 22, min at 1)
def f4(x):
    return x**2 + 2*x

# range 1 to 3 (max val at 1, min at 3)
def f5(x):
    return math.sqrt(x**5)


# TODO implement multidimensional monte carlo method 
def montecarlo_better(a,b,fn,n):
    sum = 0
    for i in range(n):
        rand_X = random.uniform(a,b)
        sum += fn(rand_X)
    b = float(b)
    return ((b - a)/n) * sum

# range (a,b) , n tries
def montecarlo_poor(a,b,fn,n,fmin,fmax):
    c = 0  # good shots
    x = np.random.uniform(a,b,n)
    y = np.random.uniform(fmin,fmax,n)
    
    for i in range(len(y)):
        if y[i] > 0 and y[i] < fn(x[i]):
            c += 1
        if y[i] < 0 and y[i] > fn(x[i]):
            c += 1

    return (fmax - fmin) * (float(b) - a) * (float(c) / n)

def cone(n):
    c = 0
    h = 10
    r = 10
    ymax = xmax = 2*r
    zmax = h
    for i in range(n):
        x = np.random.rand()*xmax - xmax/2
        y = np.random.rand()*ymax - ymax/2
        z = np.random.rand()*xmax
        if x**2 + y**2 <= (r - z*r/h)**2:
            c += 1
    
    return (c/n) * xmax * ymax * zmax

def sphere(n):
    c = 0
    x = np.random.uniform(-5,5,n)
    y = np.random.uniform(-5,5,n)
    z = np.random.uniform(-5,5,n)
    for i in range(n):
        if x[i]**2 + y[i]**2 + z[i]**2 < 25:
            c += 1
    return 1000 * c/n

def weird_case(n):
    r = 10
    r1 = 3
    maxi = 2 * r
    h = 6
    c = 0
    for _ in range(n):
        x = np.random.rand()*maxi - maxi/2
        y = np.random.rand()*maxi - maxi/2
        z = np.random.rand()*maxi - maxi/2
        if x**2 + y**2 + z**2 <= r**2 and (x**2 + y**2 > r1**2 or z > h or z < 0):
            c += 1
    return (c/n) * maxi ** 3

def tests_basic(a,b,fn,fmin,fmax,expected):
    n = [10,100,1000,10000,100000]
    for i in n:
        ans = montecarlo_poor(a,b,fn,i,fmin,fmax)
        print("n =",i)
        print("wynik:",ans,"error:",abs(ans - expected))

def tests_better(a,b,fn,expected):
    n = [10, 100, 1000, 10000, 100000]
    for i in n:
        ans = montecarlo_better(a,b,fn,i)
        print("n =",i)
        print("wynik:",ans,"error:",abs(ans - expected))

#Basic Monte Carlo tests
def test1():
    print("tests of basic montecarlo:")
    print("fn = x")
    tests_basic(0,2,lin,0,2,2)
    print("fn = 1/(x^2)")
    tests_basic(1,2,f1,f1(2),f1(1),0.5)
    print("fn = 1/math.sqrt(x**5 + 8)")
    tests_basic(1,6,f2,f2(6),f2(1),0.4350597200114438)
    print("fn  = 1/math.sqrt(x+8)")
    tests_basic(1,22,f3,f3(22),f3(1),4.954451150103322)
    print("fn = x**2 + 2*x")
    tests_basic(1,22,f4,f4(1),f4(22),4032)
    print("fn = math.sqrt(x**5)")
    tests_basic(1,3,f5,f5(1),f5(3),13.07582051553134)

#'Extended' Monte Carlo tests
def test2():
    print("tests of better montecarlo:")
    print("fn = x")
    tests_better(0,2,lin,2)
    print("fn = 1/(x^2)")
    tests_better(1,2,f1,0.5)
    print("fn = 1/math.sqrt(x**5 + 8)")
    tests_better(1,6,f2,0.4350597200114438)
    print("fn  = 1/math.sqrt(x+8)")
    tests_better(1,22,f3,4.954451150103322)
    print("fn = x**2 + 2*x")
    tests_better(1,22,f4,4032)
    print("fn = math.sqrt(x**5)")
    tests_better(1,3,f5,13.07582051553134)


#calculating sphere volume tests
def test3():
    n = [10,100,1000,10000,100000,1000000]
    for i in n:
        print("n =",i)
        ans = sphere(i)
        print("wynik:",ans,"error:",abs(ans - 523.598775598))



#calculating sphere volume tests
def test4():
    n = [10,100,1000,10000,100000,1000000]
    for i in n:
        print("n =",i)
        ans = cone(i)
        print("wynik:",ans,"error:",abs(ans - (1/3 * math.pi * 1000)))

#calculating sphere volume tests
def test5():
    n = [10,100,1000,10000,100000,1000000]
    for i in n:
        print("n =",i)
        ans = weird_case(i)
        print("wynik:",ans,"error:",abs(ans - 4019.144201492542))


def main():
    #test1()
    #test2()
    #test3()
    #test4()
    test5()


if __name__ == "__main__":
    main()