import reflectString

def test_case1():
	assert reflectString.reflectString("name") == "mznv"

def test_case2():
        assert reflectString.reflectString("abyz") == "zyba"

def test_case3():
        assert reflectString.reflectString("nnnnn") == "mmmmm"

def test_case4():
        assert reflectString.reflectString("pqr") == "kji"

def test_case5():
        assert reflectString.reflectString("codesignal") == "xlwvhrtmzo"
