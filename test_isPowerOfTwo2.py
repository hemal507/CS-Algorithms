import isPowerOfTwo2


def test_case1():
    assert isPowerOfTwo2.isPowerOfTwo2(64) == True


def test_case2():
    assert isPowerOfTwo2.isPowerOfTwo2(5) == False


def test_case3():
    assert isPowerOfTwo2.isPowerOfTwo2(1) == True


def test_case4():
    assert isPowerOfTwo2.isPowerOfTwo2(16) == True


def test_case5():
    assert isPowerOfTwo2.isPowerOfTwo2(7) == False


def test_case6():
    assert isPowerOfTwo2.isPowerOfTwo2(17179869184) == True


def test_case7():
    assert isPowerOfTwo2.isPowerOfTwo2(34359738368) == True


def test_case8():
    assert isPowerOfTwo2.isPowerOfTwo2(68719476736) == True


def test_case9():
    assert isPowerOfTwo2.isPowerOfTwo2(41) == False


def test_case10():
    assert isPowerOfTwo2.isPowerOfTwo2(239) == False


def test_case11():
    assert isPowerOfTwo2.isPowerOfTwo2(137438953472) == True
