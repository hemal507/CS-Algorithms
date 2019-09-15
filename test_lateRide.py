import lateRide

def test_case1() :
	assert lateRide.lateRide(240) == 4

def test_case2() :
	assert lateRide.lateRide(808) == 14

def test_case3() :
	assert lateRide.lateRide(0) == 0

def test_case4() :
	assert lateRide.lateRide(1439) == 19

def test_case5():
	assert lateRide.lateRide(8) == 8
