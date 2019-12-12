import superPrize

def test_case1() :
	assert superPrize.superPrize([12, 43, 13, 465, 1, 13], 2, 3 ) == [4]

def test_case2() :
        assert superPrize.superPrize([], 2, 2) == []

def test_case3() :
        assert superPrize.superPrize([988, 126, 876, 615, 323, 835, 815, 2, 867, 952, 95, 397, 546, 762, 350], 17, 7 ) == []

def test_case4() :
        assert superPrize.superPrize([41, 51, 91, 72, 71, 30, 28, 35, 55, 62, 65, 45, 100, 54, 83, 69, 66, 43], 2, 5) == [6, 8, 12]

def test_case5() :
        assert superPrize.superPrize([64, 67, 86, 87, 69, 49, 47, 75, 43, 74, 23, 47, 77, 83, 67, 24, 11, 59, 19, 88], 4, 5) == [8]

