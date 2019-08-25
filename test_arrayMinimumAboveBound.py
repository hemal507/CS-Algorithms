import arrayMinimumAboveBound

def test_case1() :
	assert arrayMinimumAboveBound.arrayMinimumAboveBound([1, 3, 5, 4, 2, 6],3) == 4

def test_case2() :
	assert arrayMinimumAboveBound.arrayMinimumAboveBound([-1, -4, -10, -5, -2],-5) == -4

def test_case3() :
	assert arrayMinimumAboveBound.arrayMinimumAboveBound([0, -2, 5, 6, -9],5) == 6

