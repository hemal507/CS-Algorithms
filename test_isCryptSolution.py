import isCryptSolution


def test_case1():
    assert isCryptSolution.isCryptSolution(["SEND", "MORE", "MONEY"],
                                           [["O", "0"], ["M", "1"], ["Y", "2"], ["E", "5"], ["N", "6"], ["D", "7"],
                                            ["R", "8"], ["S", "9"]]) == True


def test_case2():
    assert isCryptSolution.isCryptSolution(["TEN", "TWO", "ONE"],
                                           [["O", "1"], ["T", "0"], ["W", "9"], ["E", "5"], ["N", "4"]]) == False


def test_case3():
    assert isCryptSolution.isCryptSolution(["A", "A", "A"], [["A", "0"]]) == True


def test_case4():
    assert isCryptSolution.isCryptSolution(["AA", "AA", "AA"], [["A", "0"]]) == False


def test_case5():
    assert isCryptSolution.isCryptSolution(["A", "A", "A"], [["A", "1"]]) == False


def test_case6():
    assert isCryptSolution.isCryptSolution(["ONE", "ONE", "TWO"],
                                           [["O", "2"], ["T", "4"], ["W", "6"], ["E", "1"], ["N", "3"]]) == True


def test_case7():
    assert isCryptSolution.isCryptSolution(["ONE", "ONE", "TWO"],
                                           [["O", "0"], ["T", "1"], ["W", "2"], ["E", "5"], ["N", "6"]]) == False


def test_case8():
    assert isCryptSolution.isCryptSolution(["A", "B", "C"], [["A", "5"], ["B", "6"], ["C", "1"]]) == False


def test_case9():
    assert isCryptSolution.isCryptSolution(["AA", "AA", "BB"], [["A", "1"], ["B", "2"]]) == True


def test_case10():
    assert isCryptSolution.isCryptSolution(["BAA", "CAB", "DAB"],
                                           [["A", "0"], ["B", "1"], ["C", "2"], ["D", "4"]]) == False
