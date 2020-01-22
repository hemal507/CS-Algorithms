import excelSheetColumnNumber


def test_case1():
    assert excelSheetColumnNumber.excelSheetColumnNumber('AB') == 28


def test_case2():
    assert excelSheetColumnNumber.excelSheetColumnNumber('A') == 1


def test_case3():
    assert excelSheetColumnNumber.excelSheetColumnNumber('ZZ') == 702


def test_case4():
    assert excelSheetColumnNumber.excelSheetColumnNumber('OPQ') == 10573


def test_case5():
    assert excelSheetColumnNumber.excelSheetColumnNumber('DEAD') == 73714


def test_case6():
    assert excelSheetColumnNumber.excelSheetColumnNumber('SHEET') == 8826682


def test_case7():
    assert excelSheetColumnNumber.excelSheetColumnNumber('RABBIT') == 214358502
