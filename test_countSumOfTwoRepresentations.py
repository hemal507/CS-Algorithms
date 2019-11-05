import countSumOfTwoRepresentations

def test_case1():
	assert countSumOfTwoRepresentations.countSumOfTwoRepresentations(6,2,4) == 2

def test_case2():
        assert countSumOfTwoRepresentations.countSumOfTwoRepresentations(10,9,11) == 0

def test_case3():
        assert countSumOfTwoRepresentations.countSumOfTwoRepresentations(24,8,16) == 5

def test_case4():
        assert countSumOfTwoRepresentations.countSumOfTwoRepresentations(24,12,12) == 1

