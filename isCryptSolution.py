"""
def isCryptSolution(crypt, solution):
    c0,c1,c2 = [],[],[]
    for i in crypt[0] :
        for j in solution :
            if j[0] == i :
                c0.append(j[1])
    for i in crypt[1] :
        for j in solution :
            if j[0] == i :
                c1.append(j[1])
    for i in crypt[2] :
        for j in solution :
            if j[0] == i :
                c2.append(j[1])
    if (c2[0] == '0' or c0[0] == '0' or c1[0] == '0') and len(c2) > 1 :
        return False

    return int(''.join(c0) ) + int(''.join(c1)) == int(''.join(c2))
"""


def isCryptSolution(c, s):
    r = []
    for x in c:
        r.append([z[1] for y in x for z in s if z[0] == y])
    if any([x[0] == '0' for x in r]) and len(r[-1]) > 1:
        return False
    return sum(map(int, [''.join(x) for x in r[:2]])) == int(''.join(r[-1]))


print(isCryptSolution(['SEND', 'MORE', 'MONEY'],
                      [['O', '0'], ['M', '1'], ['Y', '2'], ['E', '5'], ['N', '6'], ['D', '7'], ['R', '8'], ['S', '9']]))
