import constructShell

def test_case1() :
	assert constructShell.constructShell(3) == [[0], [0, 0], [0, 0, 0], [0, 0], [0]]

def test_case2() :
	assert constructShell.constructShell(1) == [[0]] 

def test_case3() :
	assert constructShell.constructShell(5) == [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0], [0, 0], [0]]


