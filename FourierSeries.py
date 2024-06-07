
import sympy

x = sympy.Symbol('x') #variable
p = sympy.Symbol('p') #half-period
pie = sympy.pi

f = x

list_a = [0]; list_b = [0];
series_size = 10;

def delta(index, z):
    return sympy.cos((pie * index)/p * x - (z)*(pie)/2)

def build_list_a():
    a_0 = sympy.integrate(f, (x, -p, p)) / (2 * p)
    list_a[0] = a_0;
    
    for i in range(1, series_size):
        a_i = sympy.integrate(f * delta(i, 0), (x, -p, p)) / p
        list_a.append(a_i)

def build_list_b():
    
    for i in range(1, series_size):
        b_i = sympy.integrate(f * delta(i, 1), (x, -p, p)) / p
        list_b.append(b_i)
