import sympy as sp
x = sp.Symbol('x')

def f(x):
    return 2 * x + 1

def g(x):
    return 3*x + 5


def composite_func(f, g ,x):
    return f(g(x))



if __name__ == "__main__":
    
    result = composite_func(f,g,x)
    print("equation of h(x)-----------------------")
    print('h(x) = ' + str(result))
    x_val = float(input("Enter the value of x: "))
    value = composite_func(f, g, x_val)
    print('h(x) = ' + str(value))
    print()


