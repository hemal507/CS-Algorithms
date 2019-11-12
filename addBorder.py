def addBorder(p):
        l=len
        b='*'*(l(p[0])+2)
        p.insert(0,b)
        p.insert(l(p)+1,b)
        for i in range(1,l(p)-1) :
                p[i] = '*' + p[i] + '*'
        return p

print(addBorder(["1234","5678"]))

		

