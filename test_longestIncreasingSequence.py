import longestIncreasingSequence


def test_case1():
    assert longestIncreasingSequence.longestIncreasingSequence([10, 22, 9, 33, 21, 50, 41, 60]) == 5


def test_case2():
    assert longestIncreasingSequence.longestIncreasingSequence([1, -1]) == 1


def test_case3():
    assert longestIncreasingSequence.longestIncreasingSequence([1, 1]) == 1


def test_case4():
    assert longestIncreasingSequence.longestIncreasingSequence([1, -1, -2, -99]) == 1


def test_case5():
    assert longestIncreasingSequence.longestIncreasingSequence([-99, -4, -1, -1, 0, 99, 800]) == 6


def test_case6():
    assert longestIncreasingSequence.longestIncreasingSequence([-99, -4, -1, 0, 99, 800]) == 6
