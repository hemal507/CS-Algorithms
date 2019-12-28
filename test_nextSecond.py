import nextSecond

def test_case1() :
	assert nextSecond.nextSecond([23, 59, 59]) == [0, 0, 0]

def test_case2() :
        assert nextSecond.nextSecond([2, 3, 2]) == [2, 3, 3]

def test_case3() :
        assert nextSecond.nextSecond( [2, 3, 59]) ==  [2, 4, 0]

def test_case4() :
        assert nextSecond.nextSecond( [22, 59, 59]) == [23, 0, 0]


