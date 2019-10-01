import kthPermutation

def test_case1() :
	assert kthPermutation.kthPermutation( [1, 2, 3, 4, 5] ,4 ) == [1, 2, 4, 5, 3]

def test_case2() :
        assert kthPermutation.kthPermutation([1,2],1) == [1,2]

def test_case3() :
        assert kthPermutation.kthPermutation([11, 22, 31, 43, 56],120) == [56, 43, 31, 22, 11]

def test_case4() :
        assert kthPermutation.kthPermutation([14, 25, 27, 29, 30, 40, 55, 89, 100, 239], 238) == [14, 25, 27, 29, 40, 239, 100, 55, 89, 30]

def test_case5() :
        assert kthPermutation.kthPermutation([14, 25, 27, 29, 30, 40, 55, 89, 100, 239], 3628800) == [239, 100, 89, 55, 40, 30, 29, 27, 25, 14]
