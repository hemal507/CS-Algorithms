from itertools import combinations as c
def tripletSum(x, a) :
    return any( [ sum(i) == x for i in list(c(a,3))  ])


print(tripletSum(6,[2,3,1]))
#print(tripletSum(15,  [14, 1, 2, 3, 8, 15, 3]))