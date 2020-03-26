import isUnstablePair


def test_case1():
    assert isUnstablePair.isUnstablePair("aa", "AAB") == True


def test_case2():
    assert isUnstablePair.isUnstablePair("A", "z") == False


def test_case3():
    assert isUnstablePair.isUnstablePair("yyyyyy", "Azzzzzzzzz") == False


def test_case4():
    assert isUnstablePair.isUnstablePair("mehOu", "mehau") == True


def test_case5():
    assert isUnstablePair.isUnstablePair("aaZ", "AAzz") == True


def test_case6():
    assert isUnstablePair.isUnstablePair("qwerTyu123", "qwertyu") == True


def test_case7():
    assert isUnstablePair.isUnstablePair("123za", "123Z") == False


def test_case8():
    assert isUnstablePair.isUnstablePair("zzzzzAa123", "zzzzzaa") == True
