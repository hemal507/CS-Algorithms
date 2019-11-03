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

# using memoization
fib_cache = {}
def fib(n) :
        if n in fib_cache :
                return fib_cache[n]

        if n == 1 :
                return 1
        elif n == 2 :
                return 1
        elif n > 2 :
                value = fib(n-1) + fib(n-2)

        fib_cache[n] = value
        return value

