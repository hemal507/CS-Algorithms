import alternatingSort

def test_case1() :
	assert alternatingSort.alternatingSort([1, 3, 5, 6, 4, 2]) == True

def test_case2() :
	assert alternatingSort.alternatingSort([1, 4, 5, 6, 3]) == False

def test_case3() :
	assert alternatingSort.alternatingSort([-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]) == False

