def numberOfOperations(a, b):
    i=0
    while True :
        if a%b == 0 :
            a = a/b
            i += 1
        elif b%a == 0 : 
            b = b/a
            i += 1
        else :
            return i


