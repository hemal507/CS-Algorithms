import reduceString

def test_case1() :
	assert reduceString.reduceString("abacaba") == ""

def test_case2() :
	assert  reduceString.reduceString("12133221") == "1332"

def test_case3():
	assert reduceString.reduceString("") == ""
