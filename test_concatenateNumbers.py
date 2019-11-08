import concatenateNumbers

def test_case1():
	assert concatenateNumbers.concatenateNumbers(23,45) == 2345

def test_case2():
        assert concatenateNumbers.concatenateNumbers(962,12345) == 96212345

def test_case3():
        assert concatenateNumbers.concatenateNumbers(00,99) == 99

def test_case4():
        assert concatenateNumbers.concatenateNumbers(-1,1) == -11
