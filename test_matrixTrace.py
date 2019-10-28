import matrixTrace

def test_case1() :
	assert matrixTrace.matrixTrace([[1,1,1],  [0,5,0],  [2,1,3]]) == 9

def test_case2() :
        assert matrixTrace.matrixTrace([[0,1,1],  [0,0,0],  [2,1,0]]) == 0

def test_case3() :
        assert matrixTrace.matrixTrace([[1,2], [3,4]]) == 5


