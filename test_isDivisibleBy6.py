import isDivisibleBy6

def test_case1() :
	assert isDivisibleBy6.isDivisibleBy6("1*0") == ["120",  "150",  "180"]

def test_case2() :
        assert isDivisibleBy6.isDivisibleBy6("*") == ["0", "6"]

def test_case3() :
        assert isDivisibleBy6.isDivisibleBy6("*1") == []

def test_case4() :
        assert isDivisibleBy6.isDivisibleBy6("81234567890*") == ["812345678904"]

def test_case5() :
        assert isDivisibleBy6.isDivisibleBy6("41*") == ["414"]

def test_case6() :
        assert isDivisibleBy6.isDivisibleBy6("34234*2") == ["3423402",  "3423432",  "3423462",  "3423492"]


