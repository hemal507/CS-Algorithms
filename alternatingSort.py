def alternatingSort(a):
    if len(a) != len(set(a)) :
        return False        
    b = [None]*(len(a))
    for i in range(len(a)) :
        if i % 2 == 0 :
            b[i] = a[i/2]
        else :
            b[i] = a[-i/2]
    
    s = sorted(b)
    if b == s :
        return True
    else  :
        return False


