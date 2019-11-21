import deleteDigit

def test_case1() :
	assert deleteDigit.deleteDigit(152) == 52

def test_case2() :
        assert deleteDigit.deleteDigit(1001) == 101

def test_case3() :
        assert deleteDigit.deleteDigit(10) == 1

def test_case4() :
        assert deleteDigit.deleteDigit(222219) == 22229

def test_case5() :
        assert deleteDigit.deleteDigit(109) == 19

def test_case6() :
        assert deleteDigit.deleteDigit(222250) == 22250

def test_case7() :
        assert deleteDigit.deleteDigit(44435) == 4445

def test_case8() :
        assert deleteDigit.deleteDigit(12) == 2

def test_case9() :
        assert deleteDigit.deleteDigit(218616) == 28616

def test_case10() :
        assert deleteDigit.deleteDigit(861452) == 86452


