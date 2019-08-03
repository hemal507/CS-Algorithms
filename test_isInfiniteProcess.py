import isInfiniteProcess

def test_negative_case1():
	assert isInfiniteProcess.isInfiniteProcess(2,6)	== False
def test_negative_case2() :
	assert isInfiniteProcess.isInfiniteProcess(2,10) == False
def test_negative_case3() :
	assert isInfiniteProcess.isInfiniteProcess(10,10) == False
def test_positive_case1() :
	assert isInfiniteProcess.isInfiniteProcess(2,3) == True
def test_positive_case2() :
	assert isInfiniteProcess.isInfiniteProcess(0,1) == True
def test_positive_case3() :
	assert isInfiniteProcess.isInfiniteProcess(3,1) == True

