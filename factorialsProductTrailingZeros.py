def factorialsProductTrailingZeros(l, r):
    t=1
    for i in range(l,r+1) :
        f=1
        for j in range(2,i+1) :
            f *= j
        t *= f
    c=0 

    for x in `t`[-1::-1] :
	if x == 'L' : 
	    continue
        if x == '0' :
            c += 1
	else :
    	    return c

print(factorialsProductTrailingZeros(5,5))
