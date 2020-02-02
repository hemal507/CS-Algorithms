"""
def surpasserCount(a):
    return sum([y > a[x] for x in range(len(a)) for y in a[x + 1:]]) % 1000000007
"""

import numpy


def surpasserCount(a):
    a = numpy.r_[a]
    print(type(a))
    r = 0
    for i in a:
        a = a[1:]
        r += (a > i).sum()
    return r


print(surpasserCount([1,2,3,4,5]))
