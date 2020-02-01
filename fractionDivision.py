def fractionDivision(a, b) :
    c = [ a[0] * b[1] , b[0] * a[1] ]
    i =min(c)
    while i >= 2 :
        if c[0] % i == 0 and c[1] % i == 0 :
            return  [ c[0] / i , c[1] / i ]
        i -= 1

print(fractionDivision([9, 4],[3, 4]))