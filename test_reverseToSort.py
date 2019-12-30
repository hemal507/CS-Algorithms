import reverseToSort

def test_case1() :
	assert reverseToSort.reverseToSort([-1, 5, 4, 3, 2, 8]) == True

def test_case2() :
        assert reverseToSort.reverseToSort([1, 3, 2, 5, 4, 6]) == False

def test_case3() :
        assert reverseToSort.reverseToSort([2, 3, 2, 4]) == False

def test_case4() :
        assert reverseToSort.reverseToSort([19, 32, 23]) == True

def test_case5() :
        assert reverseToSort.reverseToSort([-100, 4, 10, 4, 2]) == False

def test_case6() :
        assert reverseToSort.reverseToSort([76, -2, 95, 29, -47, 19, -95, 69]) == False

def test_case7() :
        assert reverseToSort.reverseToSort([-20, -58, 44, 51, 71, 98, 39, 64, -81, -18]) == False

def test_case8() :
        assert reverseToSort.reverseToSort([100, 99, 98]) == True

def test_case9() : 
        assert reverseToSort.reverseToSort([-1, 72, -12]) == False

def test_case10() :
        assert reverseToSort.reverseToSort([-46, 26, -9, 63]) == True
