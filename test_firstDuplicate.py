import firstDuplicate

def test_case1() :
	assert firstDuplicate.firstDuplicate2([23,5,6,7,7,6,7,23,1]) == 7
	
def test_case2() :
	assert firstDuplicate.firstDuplicate2([1,2,3,45,6,7,8,9,0]) == -1
