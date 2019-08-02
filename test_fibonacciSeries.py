import fibonacciSeries

def test_case1() :
	assert fibonacciSeries.fibonacciGenerator(9,0,1) == 34 

def test_case2() :
	assert fibonacciSeries.fibonacciGenerator(0,0,1) == 0

def test_case3() :
	assert fibonacciSeries.fibonacciGenerator(1,0,1) == 1 

def test_case4() :
	assert fibonacciSeries.fibonacciGenerator(2,0,1) == 1

def test_case5() :
	assert fibonacciSeries.fibonacciGenerator(3,0,1) == 2


