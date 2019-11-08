import swapNeighbouringDigits

def test_case1() :
	assert swapNeighbouringDigits.swapNeighbouringDigits(1234) == 2143

def test_case2():
	assert swapNeighbouringDigits.swapNeighbouringDigits(12345678) == 21436587

def test_case3():
	assert swapNeighbouringDigits.swapNeighbouringDigits(9340) == 3904 
