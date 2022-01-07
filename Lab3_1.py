import cmath


def f(x, coeff):
    c = -(coeff[0]*(x**2)+coeff[1]*x)
    return c


x = float(input())
coeff = [2, 1]
print(f(x, coeff))


