import fibonacciSum

def test_case1() :
	assert fibonacciSum.fibonacciSum(20) == [2,5,13]

def test_case2() :
	assert fibonacciSum.fibonacciSum(21) == [21]

def test_case3() :
	assert fibonacciSum.fibonacciSum(33) == [1,3,8,21]
