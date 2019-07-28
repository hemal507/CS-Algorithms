def addDigits(a, b, n):
	for i in range(n) :
		for j in range(0,10) :
        		r = int(str(a) + str(j))
        		if r % b == 0 :
          			a = r
          			break
	return a      

print(addDigits(12,11,2))

