import cyclicName

def test_case1() :
	assert cyclicName.cyclicName("nicecoder", 15) == "nicecoderniceco"

def test_case2() :
	assert cyclicName.cyclicName("codesignal",50) == "codesignalcodesignalcodesignalcodesignalcodesignal"

def test_case3() :
	assert cyclicName.cyclicName("test",4) == "test"

def test_case4() :
	assert cyclicName.cyclicName("q",8) == "qqqqqqqq"

def test_case5():
	assert cyclicName.cyclicName("negativetest",4) == "nega"
