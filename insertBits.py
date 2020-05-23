def insertBits(n, a, b, k):
    nb = '0'*b + bin(n)[2:]
    kb = bin(k)[2:]
    if len(kb) < (b-a)+1 :
        kb = '0'*(len(kb) - (b-a) + 1) + kb
    return int(nb[:-b-1] + kb + nb[len(nb)-a:],2)
