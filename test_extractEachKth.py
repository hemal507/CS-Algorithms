import extractEachKth

def test_case1() :
	assert extractEachKth.extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3) == [1, 2, 4, 5, 7, 8, 10]

def test_case2() :
        assert extractEachKth.extractEachKth([1, 1, 1, 1, 1],1) == []

def test_case3() :
        assert extractEachKth.extractEachKth([1, 2, 1, 2, 1, 2, 1, 2],2) == [1, 1, 1, 1]

def test_case4() :
        assert extractEachKth.extractEachKth([1, 2, 1, 2, 1, 2, 1, 2],10) == [1, 2, 1, 2, 1, 2, 1, 2]

def test_case5() :
        assert extractEachKth.extractEachKth([2, 4, 6, 8, 10],2) == [2, 6, 10]
