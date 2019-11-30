import makeArrayConsecutive

def test_case1():
	assert makeArrayConsecutive.makeArrayConsecutive([6, 2, 3, 8]) == [4, 5, 7]

def test_case2():
        assert makeArrayConsecutive.makeArrayConsecutive([-1, -3]) == [-2]

def test_case3():
        assert makeArrayConsecutive.makeArrayConsecutive([5, 4, 6]) == []

def test_case4():
        assert makeArrayConsecutive.makeArrayConsecutive([-1, 3]) == [0, 1, 2]


