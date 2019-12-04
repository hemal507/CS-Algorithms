import caesarBoxCipherEncoding

def test_case1() :
	assert caesarBoxCipherEncoding.caesarBoxCipherEncoding("a message") == "aea sgmse"

def test_case2() :
	assert caesarBoxCipherEncoding.caesarBoxCipherEncoding("sixteenletters16") == "seerietsxnt1tle6"
