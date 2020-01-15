import twoArraysNthElement


def test_case1():
    assert twoArraysNthElement.twoArraysNthElement([1, 3, 4], [2, 6, 8], 5) == 8


def test_case2():
    assert twoArraysNthElement.twoArraysNthElement([1, 2, 3], [4, 5, 6], 3) == 4


def test_case3():
    assert twoArraysNthElement.twoArraysNthElement([1, 3, 5], [2, 4], 2) == 3
