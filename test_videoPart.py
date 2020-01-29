import videoPart


def test_case1():
    assert videoPart.videoPart("02:20:00", "07:00:00") == [1, 3]


def test_case2():
    assert videoPart.videoPart("25:26:20", "25:26:20") == [1, 1]


def test_case3():
    assert videoPart.videoPart("00:02:20", "00:10:00") == [7, 30]


def test_case4():
    assert videoPart.videoPart("08:08:08", "20:20:20") == [2, 5]


def test_case5():
    assert videoPart.videoPart("00:00:07", "01:10:00") == [1, 600]


def test_case6():
    assert videoPart.videoPart("07:32:29", "10:12:51") == [1597, 2163]


def test_case7():
    assert videoPart.videoPart("01:41:59", "02:00:00") == [6119, 7200]
