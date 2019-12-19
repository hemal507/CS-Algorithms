def halvingSum(n): 
    r=n
    i=1
    while n/pow(2,i) >= 1 :
	r += n/pow(2,i)
        i+=1
    return r

print(halvingSum(25))
