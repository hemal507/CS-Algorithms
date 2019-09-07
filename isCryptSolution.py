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

