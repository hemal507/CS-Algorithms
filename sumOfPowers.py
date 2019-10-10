def sumOfPowers(n, divisor):
    s=0
    while n>0:
        n /= divisor
        s += n
    return s

