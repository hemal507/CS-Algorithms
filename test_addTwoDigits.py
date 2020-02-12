import addTwoDigits


def test_case1():
    assert addTwoDigits.addTwoDigits(29) == 11


def test_case2():
    assert addTwoDigits.addTwoDigits(48) == 12


def test_case3():
    assert addTwoDigits.addTwoDigits(10) == 1


def test_case4():
    assert addTwoDigits.addTwoDigits(25) == 7


def test_case5():
    assert addTwoDigits.addTwoDigits(52) == 7


def test_case6():
    assert addTwoDigits.addTwoDigits(99) == 18


def test_case7():
    assert addTwoDigits.addTwoDigits(90) == 9


def test_case8():
    assert addTwoDigits.addTwoDigits(44) == 8
