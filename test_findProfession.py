import findProfession


def test_case1():
    assert findProfession.findProfession(3, 3) == "Doctor"


def test_case2():
    assert findProfession.findProfession(4, 2) == "Doctor"


def test_case3():
    assert findProfession.findProfession(1, 1) == "Engineer"


def test_case4():
    assert findProfession.findProfession(8, 100) == "Engineer"


def test_case5():
    assert findProfession.findProfession(10, 470) == "Engineer"


def test_case6():
    assert findProfession.findProfession(17, 5921) == "Doctor"


def test_case7():
    assert findProfession.findProfession(20, 171971) == "Engineer"


def test_case8():
    assert findProfession.findProfession(30, 163126329) == "Doctor"
