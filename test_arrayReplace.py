import arrayReplace

def test_case1() :
	assert arrayReplace.arrayReplace( [1, 2, 1], 1,3) == [3,2,3]

def test_case2() :
	assert arrayReplace.arrayReplace( [1, 2, 3, 4, 5], 3, 0 ) == [1, 2, 0, 4, 5] 

def test_case3() :
	assert arrayReplace.arrayReplace([1, 1, 1] , 1, 10) == [10,10,10]

def test_case4() :
	assert arrayReplace.arrayReplace([10, 10], 0, 9) == [10,10]

