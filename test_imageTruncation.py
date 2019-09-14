import imageTruncation

def test_case1() :
	assert imageTruncation.imageTruncation([[0,100,100],  [1,255,103]] , 102) == [[0,100,100],  [1,102,102]]

def test_case2() :
	assert imageTruncation.imageTruncation([[0,100,100],  [1,255,103]] ,0 ) == [[0,0,0],  [0,0,0]]

def test_case3() :
	assert imageTruncation.imageTruncation([[1],  [2]] , 1 ) == [[1],  [1]]

