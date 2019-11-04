import variableName

def test_case1() :
	assert variableName.variableName("var_1__Int") == True

def test_case2() :
        assert variableName.variableName("qq-q") == False

def test_case3() :
        assert variableName.variableName("2w2") == False

def test_case4() :
        assert variableName.variableName(" variable") == False

def test_case5() :
        assert variableName.variableName("va[riable0") == False

def test_case6() :
        assert variableName.variableName("variable0") == True

def test_case7() :
        assert variableName.variableName("a") == True

def test_case8() :
        assert variableName.variableName("_Aas_23") == True

def test_case9() :
        assert variableName.variableName("a a_2") == False

def test_case10() :
        assert variableName.variableName("0ss") == False

