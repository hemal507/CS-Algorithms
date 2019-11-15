def compareIntegers(a, b):
    if len(a) > len(b) :
        return "greater"
    elif len(a) < len(b) :
        return "less"
    for i,j in zip(a,b) :
        if int(i) < int(j) :
            return "less"
        elif int(i) > int(j) :
            return "greater"
    return "equal"

def compareIntegers(a,b) :
	if int(a) > int(b) :
		return "greater"
	elif int(a) < int(b) :
		return "less"
	return "equal"

def compareIntegers(a,b) :
	r = { int(a) == int(b) : "equal" , int(a) < int(b) : "less" , int(a) > int(b) : "greater"}
	return r[True]

def compareIntegers(a,b) :
	return "less" if int(a) < int(b) else "greater" if int(a) > int(b) else "equal"
