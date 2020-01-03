def removeDuplicateStrings(a):
    r = []
    for i in a :
        if i not in r :
            r.append(i)
    return r


