import knapsackLight2

def test_case1() :
	assert knapsackLight2.knapsackLight2(5,4,8) == 'either'

def test_case2() :
        assert knapsackLight2.knapsackLight2(10,4,9) == 'second'

def test_case3() :
        assert knapsackLight2.knapsackLight2(3,3,3) == 'either'

def test_case4() :
        assert knapsackLight2.knapsackLight2(3,4,3) == 'first'

def test_case5() :
        assert knapsackLight2.knapsackLight2(5,4,9) == 'both'

def test_case6() :
        assert knapsackLight2.knapsackLight2(5,3,2) == 'none'

