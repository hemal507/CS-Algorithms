import math


def squareDigitsSequence(a0):
    r = 2
    l = [a0]
    y = sum([int(x) * int(x) for x in repr(a0)])
    while y not in l:
        r += 1
        l.append(y)
        y = (sum([int(x) * int(x) for x in repr(l)[-1]]))
    return r


def squareDigitsSequence(a0):
    r = 0,
    while a0 not in r:
        r += a0,
        a0 = sum(int(x) ** 2 for x in repr(a0))
    return len(r)


print(squareDigitsSequence(103))
