import math
VALUE_EPSILON = 1e-4

def f(X):
    return X**4+X-1

def fDeriv(X):
    return 4*X**3+1

n = 0
x_n = -2
f_value = f(x_n)
f_deriv = fDeriv(x_n)
while (abs(f_value) > VALUE_EPSILON):
    x_n = x_n - f_value/f_deriv
    n = n + 1
    f_value = f(x_n)
    f_deriv = fDeriv(x_n)
    print(n, x_n)
print("Final result: x =", x_n)
