import returnTwelve

def test_case1() :
	assert returnTwelve.returnTwelve(13) == 13 

def test_case2() :
	assert returnTwelve.returnTwelve(12) == 12

def test_case3() :
	assert returnTwelve.returnTwelve(0) == 12

def test_case4() :
	assert returnTwelve.returnTwelve(-12) == 12
