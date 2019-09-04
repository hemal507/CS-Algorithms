import fromDecimalToAnyBase

def test_case1() :
	assert fromDecimalToAnyBase.fromDecimal(2,13) == "1101"

def test_case2() :
	assert fromDecimalToAnyBase.fromDecimal(3,66) == "2110"

def test_case3() :
	assert fromDecimalToAnyBase.fromDecimal(9,381367044) == "876543210"
