import higherVersion

def test_case1() :
	assert higherVersion.higherVersion("1.2.2","1.2.0") == True

def test_case2() :
        assert higherVersion.higherVersion("1.0.5","1.1.0") == False

def test_case3() :
        assert higherVersion.higherVersion("1.1.0","1.1.5") == False

def test_case4() :
        assert higherVersion.higherVersion("10","9") == True

def test_case5() :
        assert higherVersion.higherVersion("1.0.10","1.1.5") == False

def test_case6() :
        assert higherVersion.higherVersion("1.10.2","1.2.10") == True

def test_case7() :
        assert higherVersion.higherVersion("0","0") == False

def test_case8() :
        assert higherVersion.higherVersion("4.3.22.1","4.3.22.1") == False
