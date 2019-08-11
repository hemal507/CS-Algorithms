import getPoints

def test_case1() :
	getPoints.getPoints([True, True, False, True],2)  == 5

def test_case2() :
        getPoints.getPoints([False, True, False, False],3)  == -7

