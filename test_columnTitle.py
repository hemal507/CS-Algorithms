import columnTitle

def test_case1() :
    assert columnTitle.columnTitle(16808) == 'XVL'

def test_case2() :
    assert columnTitle.columnTitle(282475250) == 'WTCPTR'


def test_case3():
    assert columnTitle.columnTitle(28) == 'AB'


def test_case4():
    assert columnTitle.columnTitle(1622650074) == 'EFNUWXF'


def test_case5():
    assert columnTitle.columnTitle(823564441) == 'BQHEHOK'


def test_case6():
    assert columnTitle.columnTitle(16531730) == 'AJDOET'


def test_case7():
    assert columnTitle.columnTitle(1954899098) == 'FHMWLNV'


def test_case8():
    assert columnTitle.columnTitle(101027545) == 'HMAZZU'


def test_case9():
    assert columnTitle.columnTitle(13) =='M'
