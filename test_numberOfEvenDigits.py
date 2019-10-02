import numberOfEvenDigits

def test_case1 () :
    assert  numberOfEvenDigits.numberOfEvenDigits(1010) == 2

def test_case2() :
    assert numberOfEvenDigits.numberOfEvenDigits(103) == 1

def test_case3() :
    assert  numberOfEvenDigits.numberOfEvenDigits(135) == 0
