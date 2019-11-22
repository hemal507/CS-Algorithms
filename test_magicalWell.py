import magicalWell

def test_case1():
	assert magicalWell.magicalWell(1, 2, 2) == 8

def test_case2():
        assert magicalWell.magicalWell(1, 1, 1) == 1

def test_case3():
        assert magicalWell.magicalWell(6, 5, 3) == 128

def test_case4():
        assert magicalWell.magicalWell(1601, 337, 0) == 0

def test_case5():
        assert magicalWell.magicalWell(1891, 352, 0) == 0

def test_case6():
        assert magicalWell.magicalWell(1936, 1835, 5) == 17800540

def test_case7():
        assert magicalWell.magicalWell(957, 57, 2) == 110113

def test_case8():
        assert magicalWell.magicalWell(687, 1337, 0) == 0

def test_case9():
        assert magicalWell.magicalWell(491, 1552, 4) == 3060400

def test_case10():
        assert magicalWell.magicalWell(1275, 362, 2) == 924738

