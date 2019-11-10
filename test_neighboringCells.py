import neighboringCells

def test_case1() :
	assert neighboringCells.neighboringCells([[0,0,0],  [0,0,0],  [0,0,0]]) == [[2,3,2],  [3,4,3],  [2,3,2]]

def test_case2() :
	assert neighboringCells.neighboringCells([[0,0,0]]) == [[1,2,1]]

def test_case3() :
	assert neighboringCells.neighboringCells([[0],  [0],  [0],  [0]]) == [[1],  [2],  [2],  [1]]
