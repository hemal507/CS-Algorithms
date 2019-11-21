def deleteDigit(n) :
	r=[]
	for i in range(len(`n`)) :
		g=list(`n`)
		del g[i]
		r.append(int(''.join(g)))
	return max(r)


print(deleteDigit(152))
