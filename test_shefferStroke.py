import shefferStroke 

def test_case1() :
	assert shefferStroke.shefferStroke(True, True) == False

def test_case2() :
        assert shefferStroke.shefferStroke(False, True) == True

def test_case3() :
        assert shefferStroke.shefferStroke(True, False) == True

def test_case4() :
        assert shefferStroke.shefferStroke(False, False) == True


