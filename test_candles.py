import candles

def test_case1() :
	assert candles.candles(5,2) == 9

def test_case2() :
	assert candles.candles(1,2) == 1

def test_case3() :
        assert candles.candles(3,3) == 4

def test_case2() :
        assert candles.candles(11,3) == 16

def test_case2() :
        assert candles.candles(15,5) == 18

def test_case2() :
        assert candles.candles(6,4) == 7
