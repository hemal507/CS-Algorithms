import fibonacciList

def test_case1() :
	assert fibonacciList.fibonacciList(6) == [[],  [0],  [0],  [0,0],  [0,0,0],  [0,0,0,0,0]]

def test_case2() :
        assert fibonacciList.fibonacciList(2) == [[],  [0]]

def test_case3() :
        assert fibonacciList.fibonacciList(3) == [[],  [0],  [0]]

def test_case4() :
        assert fibonacciList.fibonacciList(8) == [[],  [0],  [0],  [0,0],  [0,0,0],  [0,0,0,0,0],  [0,0,0,0,0,0,0,0],  [0,0,0,0,0,0,0,0,0,0,0,0,0]]


