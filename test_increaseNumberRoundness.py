import increaseNumberRoundness

def test_case1():
	assert increaseNumberRoundness.increaseNumberRoundness(11000) == False

def test_case2():
        assert increaseNumberRoundness.increaseNumberRoundness(902200100) == True

def test_case3():
        assert increaseNumberRoundness.increaseNumberRoundness(99080) == True

def test_case4():
        assert increaseNumberRoundness.increaseNumberRoundness(1022220) == True

def test_case5():
        assert increaseNumberRoundness.increaseNumberRoundness(106611) == True

def test_case6():
        assert increaseNumberRoundness.increaseNumberRoundness(234230) == True

def test_case7():
        assert increaseNumberRoundness.increaseNumberRoundness(888) == False

def test_case8():
        assert increaseNumberRoundness.increaseNumberRoundness(100) == False

def test_case9():
        assert increaseNumberRoundness.increaseNumberRoundness(1000000) == False
