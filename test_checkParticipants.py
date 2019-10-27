import checkParticipants

def test_case1():
	assert checkParticipants.checkParticipants([0, 1, 1, 5, 4, 8]) == [2]

def test_case2():
        assert checkParticipants.checkParticipants([0, 1, 2, 3, 4, 5]) == []

def test_case3():
        assert checkParticipants.checkParticipants([6]) == []

def test_case4():
        assert checkParticipants.checkParticipants([3, 3, 3, 3, 3, 3, 3, 3]) == [4,5,6,7]

def test_case5():
        assert checkParticipants.checkParticipants([0, 0, 1, 5, 5, 4, 5, 4, 10, 8]) == [1, 2, 5, 6, 7, 9]
