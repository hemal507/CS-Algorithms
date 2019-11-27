import fibonacciGenerator

def test_case1() :
	assert fibonacciGenerator.fibonacciGenerator(3) == [0, 1, 1]

def test_case2() :
        assert fibonacciGenerator.fibonacciGenerator(1) == [0]

def test_case3() :
        assert fibonacciGenerator.fibonacciGenerator(7) == [0, 1, 1, 2, 3, 5, 8]

def test_case4() :
        assert fibonacciGenerator.fibonacciGenerator(12) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_case5() :
        assert fibonacciGenerator.fibonacciGenerator(2) == [0, 1]

def test_case6() :
        assert fibonacciGenerator.fibonacciGenerator(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

