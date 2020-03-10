import kthLargestElement


def test_case1():
    assert kthLargestElement.kthLargestElement([7, 6, 5, 4, 3, 2, 1], 2) == 6


def test_case2():
    assert kthLargestElement.kthLargestElement([99, 99], 1) == 99


def test_case3():
    assert kthLargestElement.kthLargestElement([1], 1) == 1


def test_case4():
    assert kthLargestElement.kthLargestElement([2, 1], 1) == 2


def test_case5():
    assert kthLargestElement.kthLargestElement([-1, 2, 0], 2) == 0


def test_case6():
    assert kthLargestElement.kthLargestElement([3, 3, 3, 3, 3, 3, 3, 3, 3], 8) == 3


def test_case7():
    assert kthLargestElement.kthLargestElement(
        [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6], 1) == 11


def test_case8():
    assert kthLargestElement.kthLargestElement([-1, 2, 0], 3) == -1
