def equationTemplate(values) :
	for i in range(len(values)) :
		product_function = lambda x,y : x*y
		left_part  = reduce(product_function, values[:i+1])
		print(left_part)
		right_part = reduce(product_function, values[i:]  )
		print(right_part)
		if left_part == right_part :
			return True
	return False


def equationTemplate2(values) :
	a,b,c,d = values
	return a*b == c*d or a*c == b*d or a*d == b*c or a == b*c*d or b == a*c*d or c == a*b*d or d == a*b*c

