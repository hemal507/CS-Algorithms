import decipher

def test_case1() :
	assert decipher.decipher("10197115121") == "easy"

def test_case2() :
        assert decipher.decipher("98") == "b"

def test_case3() :
        assert decipher.decipher("122") == "z"

def test_case4() :
        assert decipher.decipher("1229897") == "zba"

def test_case5() :
        assert decipher.decipher("97989910010110210310410510610710810911011111211311411511611711811912012112297") == "abcdefghijklmnopqrstuvwxyza"

def test_case6() :
        assert decipher.decipher("10297115106108102108971061151041029897107106115981001029710711510010298") == "fasjlflajshfbakjsbdfaksdfb"

def test_case7() :
        assert decipher.decipher("11211111911310110810910097107108115111112119113101106107971101021101061021041149710511411497") == "powqelmdaklsopwqejkanfnjfhrairra"
