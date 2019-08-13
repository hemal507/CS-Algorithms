import equationTemplate

def test_case1() :
	assert equationTemplate.equationTemplate2([2, 4, 3, 6]) == True

def test_case2() :
	assert equationTemplate.equationTemplate2([2, 3, 30, 5]) == True

def test_case3() :
        assert equationTemplate.equationTemplate2([2, 4, 7, 6]) == False

def test_case4() :
        assert equationTemplate.equationTemplate2([0,1,1,1]) == False

