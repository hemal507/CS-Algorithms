import missingNumber


def test_case1():
    assert missingNumber.missingNumber([3, 1, 0]) == 2


def test_case2():
    assert missingNumber.missingNumber([0]) == 1


def test_case3():
    assert missingNumber.missingNumber([1, 2]) == 0


def test_case4():
    assert missingNumber.missingNumber([1, 0]) == 2


def test_case5():
    assert missingNumber.missingNumber([3, 1, 2]) == 0


def test_case6():
    assert missingNumber.missingNumber([5, 2, 1, 6, 3, 0]) == 4


def test_case7():
    assert missingNumber.missingNumber([8, 6, 7, 0, 2, 5, 4, 3]) == 1


def test_case8():
    assert missingNumber.missingNumber([2, 9, 8, 1, 3, 6, 7, 4, 5]) == 0


def test_case9():
    assert missingNumber.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_case10():
    assert missingNumber.missingNumber(
        [44, 26, 34, 25, 23, 42, 0, 43, 38, 14, 47, 19, 49, 6, 16, 41, 24, 35, 10, 4, 32, 5, 8, 15, 31, 3, 46, 22, 2,
         30, 28, 37, 1, 21, 39, 45, 9, 48, 36, 17, 7, 27, 18, 29, 13, 40, 11, 20, 12]) == 33


def test_case11():
    assert missingNumber.missingNumber(
        [45, 35, 38, 13, 12, 23, 48, 15, 44, 21, 43, 26, 6, 37, 1, 19, 22, 3, 11, 32, 4, 16, 28, 49, 29, 36, 33, 8, 9,
         39, 46, 17, 41, 7, 2, 5, 27, 20, 40, 34, 30, 25, 47, 0, 31, 42, 24, 10, 14]) == 18
