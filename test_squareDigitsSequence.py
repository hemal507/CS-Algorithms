import squareDigitsSequence


def test_case1():
    assert squareDigitsSequence.squareDigitsSequence(16) == 9


def test_case2():
    assert squareDigitsSequence.squareDigitsSequence(103) == 4


def test_case3():
    assert squareDigitsSequence.squareDigitsSequence(1) == 2


def test_case4():
    assert squareDigitsSequence.squareDigitsSequence(13) == 4


def test_case5():
    assert squareDigitsSequence.squareDigitsSequence(89) == 9


def test_case6():
    assert squareDigitsSequence.squareDigitsSequence(612) == 16
