def fibonacci(n) :
	return fibonacciGenerator(n,0,1)

def fibonacciGenerator(num,break_point1,break_point2) :
	if num == 0 :
		return break_point1
	if num == 1 :
		return break_point2
	return fibonacciGenerator(num-1, break_point2 , break_point1 + break_point2)

#print(fibonacci(9))
#print(fibonacciGenerator(9,0,1))

