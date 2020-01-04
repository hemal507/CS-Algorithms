def removeDuplicateStrings(a):
    r = []
    for i in a :
        if i not in r :
            r.append(i)
    return r

def removeDuplicateStrings(a):
    r = []
    for i in a :
        if i not in r :
            r += i,
    return r

def removeDuplicateStrings(s) :
        return sorted(set(s), key=s.index)
