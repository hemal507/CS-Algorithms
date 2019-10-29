import piecesOfDistinctLengths

def test_case1 () :
	assert piecesOfDistinctLengths.piecesOfDistinctLengths(14) == 4 

def test_case2 () :
        assert piecesOfDistinctLengths.piecesOfDistinctLengths(3) == 2 

def test_case3 () :
        assert piecesOfDistinctLengths.piecesOfDistinctLengths(4) == 2

def test_case4 () :
        assert piecesOfDistinctLengths.piecesOfDistinctLengths(7) == 3

def test_case5 () :
        assert piecesOfDistinctLengths.piecesOfDistinctLengths(10) == 4

def test_case6 () :
        assert piecesOfDistinctLengths.piecesOfDistinctLengths(15) == 5

def test_case7 () :
        assert piecesOfDistinctLengths.piecesOfDistinctLengths(100) == 13
