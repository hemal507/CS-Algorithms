import sameDigitNumber

def test_case1() :
	assert sameDigitNumber.sameDigitNumber(1111) == True

def test_case2() :
        assert sameDigitNumber.sameDigitNumber(1122) == False

def test_case3() :
        assert sameDigitNumber.sameDigitNumber(2222222) == True

def test_case4() :
        assert sameDigitNumber.sameDigitNumber(11112) == False

def test_case5() :
        assert sameDigitNumber.sameDigitNumber(54444) == False

def test_case6() :
        assert sameDigitNumber.sameDigitNumber(0) == True

def test_case7() :
        assert sameDigitNumber.sameDigitNumber(99) == True
