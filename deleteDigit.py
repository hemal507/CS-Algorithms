def deleteDigit(n) :
	r=[]
	for i in range(len(`n`)) :
		g=list(`n`)
		del g[i]
		r.append(int(''.join(g)))
	return max(r)

'''	
s = `vars()`[39:-2]
return max(int(re.sub(i, '', s, 1)) for i in s)

deleteDigit = lambda n: max(int(re.sub(e, "", `n`, 1)) for e in `n`)
'''

print(deleteDigit(152))
