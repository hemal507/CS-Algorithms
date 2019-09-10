import sumOfTwo


def test_case1():
	assert sumOfTwo.sumOfTwo([1, 2, 3] , [10, 20, 30, 40],  42 ) == True

def test_case2():
        assert sumOfTwo.sumOfTwo( [1, 2, 3] , [10, 20, 30, 40] ,  50 ) == False

def test_case3():
        assert sumOfTwo.sumOfTwo(  [] ,  [1, 2, 3, 4] ,  4 ) == False

def test_case4():
        assert sumOfTwo.sumOfTwo( [1, 2, 3] ,  [] , 1) == False

def test_case5():
        assert sumOfTwo.sumOfTwo( [17, 72, 18, 72, 73, 15, 83, 90, 8, 18] ,  [100, 27, 33, 51, 2, 71, 76, 19, 16, 43] ,  37 ) == True


