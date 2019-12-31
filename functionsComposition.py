import math

def compose(functions):
    return reduce(lambda a,b : lambda x : a(b(x)), functions,lambda x : x)

def functionsComposition(functions, x):
    return compose(map(eval, functions))(x)

