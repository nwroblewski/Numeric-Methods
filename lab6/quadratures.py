#!/usr/bin/env python
# - *- coding: utf- 8 - *-
import math

# Mikołaj Wróblewski AGH UST 3rd year 
# Numeric Methods

def linear(x):
    return x

def quadratic(x):
    return 2 * x**2

def sinusoidal(x):
    return 4 * math.sin(x)

def sinuso_cosinuso(x):
    return x * (math.sin(x) ** 2) + 2 * math.cos(x)

def exp(x):
    return math.exp(x)

def cos_exp(x):
    return math.cos((x+1)/(x**2 * 0.4)) * math.exp(x)

#we are passign interval [a,b] to the function
#as well as the number of wanted subintervals - n
#along with function which integral value we want to compute

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

def simpson_rule(a,b,n,fn):
    d_x = (float(b) - a)/n
    sum = 0

    for i in range(n):
        sum+= d_x/6 * (fn(i*d_x + a) + 4 * fn(((2*a+i*d_x + (i+1)*d_x)/2)) + fn((i+1)*d_x) + a)

    return sum

def tests(f,fn):
    i = 0
    for line in f:
        splitted = line.split(" ")
        a = float(splitted[0])
        b = float(splitted[1])
        n = int(splitted[2])
        function = splitted[3]
        if i == 0:
            print("a =",a,"b =",b)
        print("n =",n)
        expected = float(splitted[4])
        solution = fn(a,b,n,globals()[function])
        print("wynik",solution,"error",(abs(solution - expected)))
        #print(n,',',(abs(solution - expected)))  #for nice plotting
        i = (i + 1) % 10
def main():
    # print(rect_rule(0,1,10000,linear))
    # print(trapezoid_rule(0,1,5,linear))
    # print(simpson_rule(0,1,5,linear))

    #-----[TESTS]-----#

    linear_tests = open('linear_test.txt','r')
    quadratic_tests = open('quadratic_text.txt','r')
    sinusoidal_test = open('sinusoidal_test.txt','r')
    sinuso_cosinuso_test = open('sinuso_cosinuso_test.txt','r')
    exp_test = open('exp_test.txt','r')
    cos_exp_test = open('cos_exp_test.txt','r')
    
    #print("rectangle rule tests:")

    # print("f = x")
    #tests(linear_tests,rect_rule)
    # print("f = 2 * x ^ 2")
    #tests(quadratic_tests,rect_rule)
    #print("f = 4 * sin(x)")
    #tests(sinusoidal_test,rect_rule)
    #print("f = e ^ x")
    #tests(exp_test,rect_rule)
    #print("f = x*sin^2(x)+2*cos(x)")
    #tests(sinuso_cosinuso_test,rect_rule)
    #print("f = cos((x+1)/(x^2+0.04))*e^x")
    #tests(cos_exp_test,rect_rule)
    
    linear_tests.seek(0)
    quadratic_tests.seek(0)
    sinusoidal_test.seek(0)
    sinuso_cosinuso_test.seek(0)
    exp_test.seek(0)
    cos_exp_test.seek(0)

   
    # print("trapezoid rule tests:")

    # print("f = x")
    # print(" ")
    # tests(linear_tests,trapezoid_rule)
    # print("f = 2 * x ^ 2")
    # print(" ")
    # tests(quadratic_tests,trapezoid_rule)
    # print("f = 4 * sin(x)")
    # print(" ")
    # tests(sinusoidal_test,trapezoid_rule)
    # print("f = e ^ x")
    # print(" ")
    # tests(exp_test,trapezoid_rule)
    # print("f = x*sin^2(x)+2*cos(x)")
    # print(" ")
    # tests(sinuso_cosinuso_test,trapezoid_rule)
    # print("f = cos((x+1)/(x^2+0.04))*e^x")
    # print(" ")
    # tests(cos_exp_test,trapezoid_rule)
    
    linear_tests.seek(0)
    quadratic_tests.seek(0)
    sinusoidal_test.seek(0)
    sinuso_cosinuso_test.seek(0)
    exp_test.seek(0)
    cos_exp_test.seek(0)

   
    print("simpson rule tests:")

    print("f = x")
    tests(linear_tests,simpson_rule)
    print("f = 2 * x ^ 2")
    tests(quadratic_tests,simpson_rule)
    print("f = 4 * sin(x)")
    tests(sinusoidal_test,simpson_rule)
    print("f = e ^ x")
    tests(exp_test,simpson_rule)
    print("f = x*sin^2(x)+2*cos(x)")
    tests(sinuso_cosinuso_test,simpson_rule)
    print("f = cos((x+1)/(x^2+0.04))*e^x")
    tests(cos_exp_test,simpson_rule)

    #tests(quadratic_tests,rect_rule)
    print(globals()['quadratic'](2))  # used to indicate what function needs to be used
    

if __name__ == "__main__":
    main()