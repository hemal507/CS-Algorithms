import arithmeticExpression

def test_case1() :
	assert arithmeticExpression.arithmeticExpression(2, 3, 5) == True

def test_case2() :
        assert arithmeticExpression.arithmeticExpression(8, 2, 4) == True

def test_case3() :
        assert arithmeticExpression.arithmeticExpression(8, 3, 2) == False

def test_case4() :
        assert arithmeticExpression.arithmeticExpression(6, 3, 3) == True

def test_case5() :
        assert arithmeticExpression.arithmeticExpression(18, 2, 9) == True

def test_case6() :
        assert arithmeticExpression.arithmeticExpression(2, 3, 6) == True

def test_case7() :
        assert arithmeticExpression.arithmeticExpression(5, 2, 0) == False

def test_case8() :
        assert arithmeticExpression.arithmeticExpression(10, 2, 2) == False

def test_case9() :
        assert arithmeticExpression.arithmeticExpression(1, 2, 1) == False

def test_case10() :
        assert arithmeticExpression.arithmeticExpression(1, 2, 2) == True
