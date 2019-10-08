import evenNumbersBeforeFixed

def test_case1() :
	assert evenNumbersBeforeFixed.evenNumbersBeforeFixed([1, 4, 2, 6, 3, 1],6) == 2

def test_case2() :
        assert evenNumbersBeforeFixed.evenNumbersBeforeFixed([2, 2, 2, 1],3) == -1

def test_case3() :
        assert evenNumbersBeforeFixed.evenNumbersBeforeFixed([2, 3, 4, 3],3) == 1

