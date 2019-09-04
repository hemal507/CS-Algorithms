def fromDecimal(b, n):
    r=[]
    while n :
        r.append(str(n % b))
        n /= b
    return ''.join(r[::-1])

