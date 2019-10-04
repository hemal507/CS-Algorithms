def candles(c, m):
    r,l = 0 , 0
    while c >= 1 :
        r += c
        l += c
        c = l/m
        l -= c*m
        
    return r
    

print(candles(5,2))

