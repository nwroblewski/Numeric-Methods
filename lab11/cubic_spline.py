import matplotlib.pyplot as plt
from pylab import arange, plot, show
from numpy import poly1d
from math import log, e, sin, pi
from scipy.interpolate import interp1d
import numpy as np


# Mikołaj Wróblewski AGH UST 3rd year, Computer Science
# Numeric Methods


def f1(x):
    return x * sin(pi/x)

def f2(x):
    return x / (2 + x ** 2)


# Wykonuje interpolacje na zadanych punktach, a następnie zapisuje obraz do pliku filename.png
def cubic_spline(xn, a, filename):    # a = y; 
    n = len(xn)
    h = [0] * (n-1)
    alpha = [0] * (n-1)
    l = [0] * (n+1)
    u = [0] * n
    z = [0] * (n+1)
    b = [0] * n
    c = [0] * (n+1)
    d = [0] * n

    for i in range(n-1):
        h[i] = xn[i+1]-xn[i]

    for i in range(1, n-1):
        alpha[i] = (3./h[i])*(a[i+1]-a[i])-(3./h[i-1])*(a[i] - a[i-1])

    l[0] = 1
    u[0] = 0
    z[0] = 0
    for i in range(1, n-1):
        l[i] = 2*(xn[i+1] - xn[i-1]) - h[i-1]*u[i-1]
        u[i] = h[i]/l[i]
        z[i] = (alpha[i] - h[i-1]*z[i-1])/l[i]

    # l[n] = 1
    z[n] = 0
    c[n] = 0
    for j in range(n-2, -1, -1):
        c[j] = z[j] - u[j]*c[j+1]
        b[j] = (a[j+1] - a[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3.
        d[j] = (c[j+1] - c[j])/(3*h[j])

    for j in range(n-1):
        cub_plot(a[j], b[j], c[j], d[j], xn[j], xn[j+1])
    #plt.savefig("./"+filename)

    return a, b, c, d


def cub_plot(a, b, c, d, x_i, x_i_1):
    root = poly1d(x_i, True)    # (x-x_i)
    poly = a + b*root + c*(root**2) + d*(root**3)
    #tego uzywam do wpisywania do pliku, po prostu przekazuję output do pliku przez '>>'
    #print(poly)
    pts = arange(x_i, x_i_1, 0.01)
    plt.plot(pts, poly(pts), '-')


def equadistant(x0, x1, n):
    return [(x0 + i*(x1-x0)/(n-1)) for i in range(n)]

def main():
    filename = "f2_test8"
    x = equadistant(0.1,10,300)
    fx = list(map(f1,x))

    x1 = equadistant(0.1,10,1000)
    fx1 = list(map(f1,x1))

    
    plt.plot(x1,fx1,'k-')
    cubic_spline(x,fx,filename)
    

   

if __name__ == '__main__':
    main()