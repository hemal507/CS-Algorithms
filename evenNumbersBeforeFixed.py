def evenNumbersBeforeFixed(s, f):
    r=0
    for i in s :
        if i == f :
            return r
        r += i % 2 == 0 
    return -1


