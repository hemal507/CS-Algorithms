import concatenateArrays


def test_case1():
    assert concatenateArrays.concatenateArrays([2, 2, 1], [10, 11]) == [2, 2, 1, 10, 11]


def test_case2():
    assert concatenateArrays.concatenateArrays([1, 2], [3, 1, 2]) == [1, 2, 3, 1, 2]


def test_case3():
    assert concatenateArrays.concatenateArrays([1], []) == [1]


def test_case4():
    assert concatenateArrays.concatenateArrays([2, 10, 3, 9, 5, 11, 11], [4, 8, 1, 13, 3, 1, 14]) == [2, 10, 3, 9, 5,
                                                                                                      11, 11, 4, 8, 1,
                                                                                                      13, 3, 1, 14]


def test_case5():
    assert concatenateArrays.concatenateArrays([9, 6, 6, 9, 8, 14], [3, 2, 2, 5, 3, 11, 12, 9, 7, 7]) == [9, 6, 6, 9, 8,
                                                                                                          14, 3, 2, 2,
                                                                                                          5, 3, 11, 12,
                                                                                                          9, 7, 7]
