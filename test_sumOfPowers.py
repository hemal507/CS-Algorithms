import sumOfPowers

def test_case1() :
	assert sumOfPowers.sumOfPowers(6,2) == 4 

def test_case2() :
        assert sumOfPowers.sumOfPowers(12,5) == 2

def test_case3() :
        assert sumOfPowers.sumOfPowers(20,4) == 6

def test_case4() :
        assert sumOfPowers.sumOfPowers(1,2) == 0

def test_case5() :
        assert sumOfPowers.sumOfPowers(1,1000) == 0
