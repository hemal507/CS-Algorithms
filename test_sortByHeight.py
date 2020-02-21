import sortByHeight


def test_case1():
    assert sortByHeight.sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]) == [-1, 150, 160, 170, -1, -1, 180, 190]


def test_case2():
    assert sortByHeight.sortByHeight([-1, -1, -1, -1, -1]) == [-1, -1, -1, -1, -1]


def test_case3():
    assert sortByHeight.sortByHeight([4, 2, 9, 11, 2, 16]) == [2, 2, 4, 9, 11, 16]


def test_case4():
    assert sortByHeight.sortByHeight([-1]) == [-1]


def test_case5():
    assert sortByHeight.sortByHeight([2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]) == [1, -1, -1, -1, -1, -1,
                                                                                                 -1, -1, -1, -1, -1, -1,
                                                                                                 -1, 2]


def test_case6():
    assert sortByHeight.sortByHeight([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]) == [1, 3, -1, 23, 43, -1, -1, 54,
                                                                                         -1, -1, -1, 77]
