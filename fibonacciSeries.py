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

# using lru_cache Python3
from functools import lru_cache
@lru_cache(maxsize = 1000)
def fib2(n) :
        if n==1 or n== 2 :
                return 1
        else :
                return fib2(n-1) + fib2(n-2)
