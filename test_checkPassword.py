import checkPassword

def test_case1() :
	assert checkPassword.checkPassword(["hello",  "world",  "I",  "like",  "coding"],  "like") == 4

def test_case2() :
        assert checkPassword.checkPassword(["hello",  "world",  "I",  "like",  "coding"],  "qwerty123") == -1

def test_case3() :
        assert checkPassword.checkPassword(["codesignal"], "codesignal" ) == 1

def test_case4() :
        assert checkPassword.checkPassword(["123",  "456",  "qwerty",  "zzz",  "password",  "genius239",  "password"],  "password") == 5

def test_case5() :
        assert checkPassword.checkPassword(["warrior",  "ninja",  "trainee"],  "recruit") == -1

def test_case6() :
        assert checkPassword.checkPassword([],"igiveup") == -1
