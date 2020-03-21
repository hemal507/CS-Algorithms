import houseRobber


def test_case1():
    assert houseRobber.houseRobber([1, 1, 1]) == 2


def test_case2():
    assert houseRobber.houseRobber([]) == 0


def test_case3():
    assert houseRobber.houseRobber([0]) == 0


def test_case4():
    assert houseRobber.houseRobber([1]) == 1


def test_case5():
    assert houseRobber.houseRobber([0, 0]) == 0


def test_case6():
    assert houseRobber.houseRobber([2, 1]) == 2


def test_case7():
    assert houseRobber.houseRobber([0, 0, 0]) == 0


def test_case8():
    assert houseRobber.houseRobber([2, 4, 2]) == 4


def test_case9():
    assert houseRobber.houseRobber([1, 1, 1, 1]) == 2


def test_case10():
    assert houseRobber.houseRobber([2, 1, 1, 1]) == 3


def test_case12():
    assert houseRobber.houseRobber([1, 7, 9, 4]) == 11


def test_case13():
    assert houseRobber.houseRobber([2, 9, 7, 1]) == 10


def test_case14():
    assert houseRobber.houseRobber([1, 3, 1, 3, 100]) == 103


def test_case15():
    assert houseRobber.houseRobber([2, 1, 2, 6, 1, 8, 10, 10]) == 26


def test_case16():
    assert houseRobber.houseRobber(
        [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81,
         185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]) == 3365


def test_case17():
    assert houseRobber.houseRobber([82, 217, 170, 215, 153, 55, 185, 55, 185, 232, 69, 131, 130, 102]) == 1082


def test_case18():
    assert houseRobber.houseRobber([232, 161, 89, 177, 117, 212, 126, 247, 155, 197, 88, 217, 81, 207]) == 1489


def test_case19():
    assert houseRobber.houseRobber(
        [155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137, 89, 174, 66, 134, 26, 25, 205, 239, 85, 146, 73,
         55, 6, 122, 196, 128, 50, 61, 230, 94, 208, 46, 243, 105, 81, 157, 89, 205, 78, 249, 203, 238, 239, 217, 212,
         241, 242, 157, 79, 133, 66, 36, 165]) == 4517
