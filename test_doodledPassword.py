import doodledPassword


def test_case1():
    assert all([a in [[1, 2, 3, 4, 5],
                      [2, 3, 4, 5, 1],
                      [3, 4, 5, 1, 2],
                      [4, 5, 1, 2, 3],
                      [5, 1, 2, 3, 4]] for a in doodledPassword.doodledPassword([1, 2, 3, 4, 5])])


def test_case2():
    assert all([a in [[5]] for a in doodledPassword.doodledPassword([5])])


def test_case3():
    assert all([a in [[2, 2, 2, 2],
                      [2, 2, 2, 2],
                      [2, 2, 2, 2],
                      [2, 2, 2, 2]] for a in doodledPassword.doodledPassword([2, 2, 2, 2])])


def test_case4():
    assert all([a in [[9, 8, 7, 5, 4],
                      [8, 7, 5, 4, 9],
                      [7, 5, 4, 9, 8],
                      [5, 4, 9, 8, 7],
                      [4, 9, 8, 7, 5]] for a in doodledPassword.doodledPassword([9, 8, 7, 5, 4])])


def test_case5():
    assert all([a in [[1, 5, 1, 5, 1, 4],
                      [5, 1, 5, 1, 4, 1],
                      [1, 5, 1, 4, 1, 5],
                      [5, 1, 4, 1, 5, 1],
                      [1, 4, 1, 5, 1, 5],
                      [4, 1, 5, 1, 5, 1]] for a in doodledPassword.doodledPassword([1, 5, 1, 5, 1, 4])])
