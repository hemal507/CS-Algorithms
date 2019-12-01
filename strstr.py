def strstr(s, x) :
    return ([i for i in range(n) if s[i:i+l] == x ]+[-1])[0]

def strstr(s, x) :
    try :
        return s.index(x)
    except :
        return -1
