def insertDashes(s) :
	r=[s[0]]
	for i in range(len(s)-1) :
		if s[i].isalpha() and s[i+1].isalpha() :
			r += '-'+s[i+1]
		elif s[i] == ' ' :
			r += s[i] + s[i+1]
		print(r)

	return ''.join(r)


print(insertDashes('wel come'))
