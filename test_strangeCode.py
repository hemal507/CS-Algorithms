import strangeCode

def test_case1() :
	assert strangeCode.strangeCode(4,8) == 'ab'

def test_case2() :
        assert strangeCode.strangeCode(10,15) == 'ab'

def test_case3() :
        assert strangeCode.strangeCode(10,16) == 'aba'
