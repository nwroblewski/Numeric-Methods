#!/usr/bin/env python


# Mikołaj Wróblewski AGH UST 3rd year of Computer Science 
# Numeric Methods

import math
import numpy as np
# from scipy import integrate

# basic quadratures to compare with gaussian-legendre rule

def rect_rule(a,b,n,fn):
    d_x = (float(b)-a)/n # step size
    sum = 0

    for i in range(n):
        sum+= fn(a+i*d_x) * d_x

    return sum

def trapezoid_rule(a,b,n,fn):
    d_x = (float(b) - a)/n 
    sum = 0

    for i in range(n):
        sum+= fn(((2*a+i*d_x + (i+1)*d_x)/2)) * d_x

    return sum

#TODO zaimplementować normalnie tę metodę - tak żeby działała
def simpson_rule(a,b,n,fn):
    d_x = (float(b) - a)/n
    ans = 0
    sum1 = 0
    sum2 = 0
    for i in range(1,n):
        if i%2 == 0:
            sum1+= fn(a + i*d_x)
        else:
            sum2+= fn(a + i*d_x)

    ans = (d_x/3) * ( fn(a) + 4 * sum1 + 2 * sum2 + fn(b))
    return ans


# low-order quadrature rules:
# x's and weights - of course aproximated values
# for more details go to https://en.wikipedia.org/wiki/Gaussian_quadrature


x = [[0.57735,-0.57735],[0,0.774597,-0.774597],[0.339981,-0.339981,0.861136,-0.861136],
[0,0.538469,-0.538469,0.90618,-0.90618]]

w = [[1,1],[0.888889,0.555556,0.555556],[0.652145,0.652145,0.347855,0.347855],
[0.568889,0.478629,0.478629,0.236927,0.236927]]

def f1(x):
    return 3 * x**3 - 1

def f2(x):
    return 2 * x**2

def f3(x):
    return 4 * math.sin(x)

def gaussian_legendre(a,b,n,fn):
    res = 0
    if n<2:
        return None
    for i in range(n):
        res += w[n-2][i] * fn( ((b-a) * 0.5 * x[n-2][i]) + (a+b) * 0.5 )
        
    res = (b - a) * 0.5 * res
    return res

def tests_basic():
    print("TESTY DLA PRZEDZIALU [-1,1]")
    print("")
    a = -1
    b = 1
    funs = ["3 * x^3 - 1","2 * x^2","4 * sin(x)"]
    expected = [-2,1.333333333333333,0]
    functions = [f1,f2,f3]
    for i in range(3):
        print(funs[i])        
        print("error for rect_rule:", abs(rect_rule(a,b,100000,functions[i])-expected[i]))
        print("error for trapezoid rule:", abs(trapezoid_rule(a,b,100000,functions[i]) - expected[i]))
        print("error for simpson's rule:", abs(simpson_rule(a,b,100000,functions[i]) - expected[i]))
        for j in range(2,6,1):
            ans = gaussian_legendre(a,b,j,functions[i])
            print("stopien wielomianu:",j)
            print("wynik:",ans,"\terror", abs(ans - expected[i]))

    #TODO Napisać testy dla innych przedziałów        

def tests_more():
    print("")
    print("TESTY DLA PRZEDZIALU [0,20]")
    print("")
    a = 0
    b = 20
    funs = ["3 * x^3 - 1","2 * x^2","4 * sin(x)"]
    expected = [119980,5333.333333333333,2.367671752746432]
    functions = [f1,f2,f3]
    for i in range(3):
        print(funs[i])        
        print("error for rect_rule:", abs(rect_rule(a,b,100000,functions[i])-expected[i]))
        print("error for trapezoid rule:", abs(trapezoid_rule(a,b,100000,functions[i]) - expected[i]))
        print("error for simpson's rule:", abs(simpson_rule(a,b,100000,functions[i]) - expected[i]))
        for j in range(2,6,1):
            ans = gaussian_legendre(a,b,j,functions[i])
            print("stopien wielomianu:",j)
            print("wynik:",ans,"\terror", abs(ans - expected[i]))

def tests_wider():
    print("")
    print("TESTY DLA PRZEDZIALU [10,1000]")
    print("")
    a = 10
    b = 1000
    funs = ["3 * x^3 - 1","2 * x^2","4 * sin(x)"]
    expected = [749999991510,666666000,-5.605802421468622]
    functions = [f1,f2,f3]
    for i in range(3):
        print(funs[i])        
        print("error for rect_rule:", abs(rect_rule(a,b,100000,functions[i])-expected[i]))
        print("error for trapezoid rule:", abs(trapezoid_rule(a,b,100000,functions[i]) - expected[i]))
        print("error for simpson's rule:", abs(simpson_rule(a,b,100000,functions[i]) - expected[i]))
        for j in range(2,6,1):
            ans = gaussian_legendre(a,b,j,functions[i])
            print("stopien wielomianu:",j)
            print("wynik:",ans,"\terror", abs(ans - expected[i]))

def main():
    tests_basic()
    tests_more()
    tests_wider()

if __name__ == "__main__":
    main() 