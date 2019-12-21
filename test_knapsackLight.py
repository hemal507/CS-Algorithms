import knapsackLight

def test_case1() :
	assert knapsackLight.knapsackLight(10, 5, 6, 4, 8) == 10

def test_case2() :
        assert knapsackLight.knapsackLight(10, 5, 6, 4, 9) == 16

def test_case3() :
        assert knapsackLight.knapsackLight(5, 3, 7, 4, 6) == 7

def test_case4() :
        assert knapsackLight.knapsackLight(10, 2, 11, 3, 1) == 0

def test_case5() :
        assert knapsackLight.knapsackLight(15, 2, 20, 3, 2) == 15

def test_case6() :
        assert knapsackLight.knapsackLight(2, 5, 3, 4, 5) == 3

def test_case7() :
        assert knapsackLight.knapsackLight(4, 3, 3, 4, 4) == 4

def test_case8() :
        assert knapsackLight.knapsackLight(3, 5, 3, 8, 10) == 3

