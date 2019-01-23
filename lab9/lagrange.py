#!/usr/bin/env python
# - *- coding: utf- 8 - *-

# Mikołaj Wróblewski AGH UST 3rd year, Computer Science
# Numeric Methods
import operator
import functools as f
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.misc as sm

def f1(x):
    return math.sqrt(x)

def f2(x):
    return math.sin(x)

def f3(x):
    return x**3 + 2*x 


def equadistant(x0, x1, n):
    return [(x0 + i*(x1-x0)/(n-1)) for i in range(n)]

  

def lagrange(f, x, n, nodes):
    values = list(map(f, nodes))
    sum = 0
    for i in range(n):
        term = 1
        for j in range(n):
            if i != j:
                term = term * (x - nodes[j]) / (nodes[i] - nodes[j])
        term = term*values[i]
        sum += term
    return sum

def tests_with_plot(n,fn,filename):
    nodes = equadistant(0,10,n)
    interpolated = []
    forplot = equadistant(0,10,1000)
    values = list(map(fn,forplot))

    # this section is used to get list of x's in middle of interpolation points
    # as well as calculates errors of interpolation there
    in_half = equadistant(0,10,n*2 - 1)
    in_half_fin = [in_half[i] for i in range(n*2-1) if i%2==1]
    in_half_val = list(map(fn,in_half_fin))
    in_half_errors = [abs(lagrange(fn,in_half_fin[i],n,nodes) - in_half_val[i]) for i in range((n*2 - 1)//2)]
    print(in_half_fin)  #printing middle points x's
    print(in_half_errors) #printing interpolation errors for middle points
    print('')
    
    #plotting section
    for i in range(1000):
        interpolated.append(lagrange(fn,forplot[i],n,nodes))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(forplot,values,'b-',forplot,interpolated,'g-',
            nodes,list(map(fn,nodes)),'y.')
    plt.savefig('/home/mikolaj/Pulpit/MOWNIT2/lab9/' + filename + '.png')


#unfortunately not working.
def estimate_error(fn,nodes,k):
    in_half = equadistant(0,10,k*2 - 1)
    in_half_fin = [in_half[i] for i in range(k*2-1) if i%2==1]
    order = k+1
    if order%2 == 0:
        order = k+2
    deriv_vals = [sm.derivative(fn,in_half_fin[i], dx=1.0/2**20, n = k, order = order) for i in range((k*2 - 1)//2)]
    second_part_val = []
    mul = 1
    # for i in range(1000):
    #     deriv_vals.append(sm.derivative(fn,x[i],dx=1e-5,n = k,order = k + 1))
    
    for i in range((k*2 - 1)//2):
        for j in range(k):
            mul *= abs(in_half_fin[i] - nodes[j])     
        second_part_val.append(mul)
        mul = 1
    
    print(deriv_vals)
    deriv_max = max(deriv_vals)
    second_max = max(second_part_val)
    print(second_max)
    

    return (deriv_max/sm.factorial(k)) * second_max

#not working.
def error_tests():
    n = [3,4,5,8]
    for i in n:
        #print("estimated max error for f1 with",i,"interpolation nodes is:",estimate_error(f1,equadistant(0,10,i),i))
        print("estimated max error for f2 with",i,"interpolation nodes is:",estimate_error(f2,equadistant(0,10,i),i))
        print("estimated max error for f3 with",i,"interpolation nodes is:",estimate_error(f3,equadistant(0,10,i),i))
    
    print("finished")

def main():
    #tests_with_plot(8,f1,'sqrt_8_points')
    #tests_with_plot(8,f2,'sin_8_points')
    #tests_with_plot(8,f3,'qubic_8_points')
    print("Lagrange Interpolation.")

if __name__ == "__main__":
    main()