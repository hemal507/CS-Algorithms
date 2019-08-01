def almostIncreasingSequence(s):
    for i in range(len(s)) :
        t = [x[1] for x in list(enumerate(s)) if x[0] != i]
        c=1
        for j in range(len(t)-1) :
            if t[j] < t[j+1] :
                c += 1
        if c == len(t) :   
            return True
        
    return False
     

def almostIncreasingSequence2(s):
    for i in range(len(s)) :
        t = [x for x in s]
        del t[i]
        if len(t) == len(set(t)) and t == sorted(t) :    
            return True
    
    return False
    

def almostIncreasingSequence3(s):
    droppped = False
    last = prev = min(s) - 1
    for elm in s:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True




