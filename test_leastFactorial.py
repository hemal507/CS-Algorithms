import leastFactorial

def test_case1() :
	assert leastFactorial.leastFactorial(17) == 24 

def test_case2() :
	assert leastFactorial.leastFactorial(1) == 1

def test_case3() :
	 assert leastFactorial.leastFactorial(5) == 6

def test_case4():
	 assert leastFactorial.leastFactorial(55) == 120
