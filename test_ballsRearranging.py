import ballsRearranging


def test_case1():
    assert ballsRearranging.ballsRearranging([6, 4, 1, 7, 10]) == 2


def test_case2():
    assert ballsRearranging.ballsRearranging([25]) == 0


def test_case3():
    assert ballsRearranging.ballsRearranging([25, 23]) == 1


def test_case4():
    assert ballsRearranging.ballsRearranging([25, 24]) == 0


def test_case5():
    assert ballsRearranging.ballsRearranging([2, 5, 4]) == 1


def test_case6():
    assert ballsRearranging.ballsRearranging([2, 7, 6, 1]) == 2


def test_case7():
    assert ballsRearranging.ballsRearranging([2, 27, 16, 5, 21, 3, 25, 28, 7, 10]) == 5


def test_case8():
    assert ballsRearranging.ballsRearranging(
        [74, 34, 69, 71, 89, 85, 73, 88, 38, 43, 2, 27, 84, 11, 48, 99, 61, 15, 66, 81, 3, 51, 26, 63, 94, 24, 70, 93,
         12, 1, 78, 32, 55, 62, 96, 33, 75, 54, 92, 95, 13, 53, 36, 28, 64, 49, 65, 72, 31, 45]) == 20


def test_case9():
    assert ballsRearranging.ballsRearranging(
        [5, 73, 96, 228, 963, 694, 485, 700, 430, 886, 60, 291, 829, 27, 185, 667, 659, 879, 167, 603, 80, 677, 837,
         693, 802, 109, 722, 953, 423, 163, 821, 63, 650, 927, 406, 67, 935, 328, 114, 403, 281, 811, 778, 789, 685,
         556, 538, 377, 479, 547]) == 43
