import math
def primesSum(a, b):
    return sum([ x for x in range(a if a>1 else a+1,b+1) if  all([x %i !=0 for i in range(2, int(math.sqrt(x))+1 ) ]) ])

