import isIdentityMatrix

def test_case1():
	assert isIdentityMatrix.isIdentityMatrix([[1,0,0],  [0,1,0],  [0,0,1]]) == True

def test_case2():
        assert isIdentityMatrix.isIdentityMatrix([[1,0,0],  [0,0,0],  [0,0,1]]) == False

def test_case3():
        assert isIdentityMatrix.isIdentityMatrix([[1,1,0],  [0,1,0],  [0,0,1]]) == False

def test_case4():
        assert isIdentityMatrix.isIdentityMatrix([[1,0],  [0,1]]) == True

def test_case5():
        assert isIdentityMatrix.isIdentityMatrix([[0,0,0],  [0,1,0],  [0,0,1]]) == False

def test_case6():
        assert isIdentityMatrix.isIdentityMatrix([[1,0,0,0],  [0,5,0,0],  [0,0,0,0],  [0,0,0,5]]) == False
