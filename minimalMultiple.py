def minimalMultiple(d, l):
    for i in range(1,l+1) :
        if i*d >= l :
            return i*d
