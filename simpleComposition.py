import math

def compose(f, g):
    return lambda x : f(g(x))

def simpleComposition(f, g, x):
    return compose(eval(f), eval(g))(x)

print(simpleComposition("math.log10","abs",-100))
