import crossingSum

def test_case1() :
	assert crossingSum.crossingSum([[1,1,1,1],  [2,2,2,2],  [3,3,3,3]], 1, 3) == 12

def test_case2() :
        assert crossingSum.crossingSum([[1,1],  [1,1]], 0, 0) == 3

def test_case3() :
        assert crossingSum.crossingSum([[1,1],  [3,3],  [1,1],  [2,2]], 3, 0) == 9

def test_case4() :
        assert crossingSum.crossingSum([[100]], 0, 0 ) == 100

def test_case5() :
        assert crossingSum.crossingSum([[1,2],  [3,4]], 1, 1) == 9

def test_case6() :
        assert crossingSum.crossingSum([[1,2,3,4]], 0, 3) == 10

def test_case7() :
        assert crossingSum.crossingSum([[1,2,3,4,5],  [1,2,2,2,2],  [1,2,2,2,2],  [1,2,2,2,2],  [1,2,2,2,2],  [1,2,2,2,2],  [1,2,2,2,2]], 1 , 1) == 21

