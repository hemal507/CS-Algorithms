import replaceAllDigitsRegEx

def test_case1():
	assert replaceAllDigitsRegEx.replaceAllDigitsRegEx("There are 12 points") == "There are ## points"

def test_case2():
        assert replaceAllDigitsRegEx.replaceAllDigitsRegEx("012ss210") == "###ss###"

def test_case3():
        assert replaceAllDigitsRegEx.replaceAllDigitsRegEx(" _Aas 23") == " _Aas ##"

def test_case4():
        assert replaceAllDigitsRegEx.replaceAllDigitsRegEx("no digits here") == "no digits here"

def test_case5():
        assert replaceAllDigitsRegEx.replaceAllDigitsRegEx(" aa_0239mehce3d") == " aa_####mehce#d"

def test_case6():
        assert replaceAllDigitsRegEx.replaceAllDigitsRegEx("v z gv4zyx eu mu ") == "v z gv#zyx eu mu "
