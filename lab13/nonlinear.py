

import math as math
import numpy as np

def f1(x):
    return 2 * x**2 + 1 - 2**x

def f1prime(x):
    return 4 * x - 2 ** x * math.log(2) 

def f1a(x1,x2,x3):
    return x1**2 + x2**2 + x3**2

def f2a(x1,x2,x3):
    return 2 * x1 **2 + x2 ** 2 - 4 * x3

def f3a(x1,x2,x3):
    return 3 * x1 ** 2 - 4 * x2 + x3 ** 2 

def secant(a,b,f,eps,maxiter):
    x = [a,b]
    x0 = a
    x1 = b
    i = 0 #iteration counter
    while abs(x0-x1) > eps:
        x0 = x[len(x) - 2]
        x1 = x[len(x) - 1]
        x.append(x1 - f(x1)*((x1-x0)/(f(x1) - f(x0))))
        i += 1
        if(i > maxiter):
            break

    return x[len(x) - 1],i

def newton(x0,f,fprime,maxiter):
    j = 0
    xprev = x0+100
    for i in range(maxiter):
        if(abs(fprime(x0)) > 1e-10):
            x0 = x0 - f(x0)/fprime(x0)
            if(abs(x0 - xprev) < 1e-10):
                break
            j += 1
        else:
            break
        xprev = x0
    return x0,j

#TODO implement newton-raphson method for systems of nonlinear equations

#evaluates given jacobian value
def jacobian(x,y,z,jac):
    matrix = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            matrix[i][j] = jac[i][j](x,y,z)
    return matrix

#x0 is starting vector presented by np.array
def newton_raphson(x0, maxiter):
    # hardcoded Jacobian of f1,f2,f3
    primes = np.array([[lambda x,y,z: 2*x,lambda x,y,z:  2*y, lambda x,y,z: 2*z],
        [lambda x,y,z: 4 * x, lambda x,y,z:  2 * y, lambda x,y,z:  -4],
        [lambda x,y,z:  6 * x,lambda x,y,z:  -4, lambda x,y,z:  2 * z ]])

    for i in range(maxiter):
        f = np.array([f1a(x0[0],x0[1],x0[2]),f2a(x0[0],x0[1],x0[2]),f3a(x0[0],x0[1],x0[2])])
        try:    #in case jacobian isn't invertible
            c = np.linalg.inv(jacobian(x0[0],x0[1],x0[2],primes))
        except:
            return x0,'Jacobian not invertible at iteration:',i
        c = c @ f
        xprev = x0
        x0 = x0 - c
        if(np.allclose(x0,xprev,atol=1e-8)):
            break

    return x0

def main():
    print("secant method")
    print(secant(-1,10,f1,1e-10,100))
    print(secant(5,10,f1,1e-10,100))
    print(secant(0.3,2,f1,1e-10,100))

    print("newton-raphson method for first function")
    print(newton(6,f1,f1prime,100))
    print(newton(4,f1,f1prime,100))
    print(newton(0,f1,f1prime,100))
    print("newton-raphson for system of nonlinear equations")
    print(newton_raphson(np.array([10,0,0]),1000))

if __name__ == '__main__':
    main()