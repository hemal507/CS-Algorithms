import insertDashes

def test_case1() :
	assert insertDashes.insertDashes("aba caba") == "a-b-a c-a-b-a"

def test_case2() :
        assert insertDashes.insertDashes("x") == "x"
