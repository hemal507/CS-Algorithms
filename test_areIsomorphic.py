import areIsomorphic

def test_case1() :	
	assert areIsomorphic.areIsomorphic([[1,1,1],  [0,0]], [[2,1,1],  [2,1]]) == True

def test_case2() :
        assert areIsomorphic.areIsomorphic([[2],  []] , [[2]]) == False

def test_case3() :
        assert areIsomorphic.areIsomorphic([[2],  [1],  [3,5]] ,[[],  [1],  [1,6]]) == False

def test_case4() :
        assert areIsomorphic.areIsomorphic([[1,1,1],  [0,0]], [[2,1,3],  [2,0],  []]) == False

def test_case5() :
        assert areIsomorphic.areIsomorphic([[],  [1]], [[],  [6,2,5]]) == False

def test_case6() :
        assert areIsomorphic.areIsomorphic([[1,3,4],  []], [[2,1,2],  []]) == True

def test_case7() :
        assert areIsomorphic.areIsomorphic([[]],[[]]) == True

def test_case8() :
        assert areIsomorphic.areIsomorphic([[2],  [1],  [3,50,33]], [[],  [1],  [1,6,32]]) == False

def test_case9() :
        assert areIsomorphic.areIsomorphic([[6],  [3,5,2,4]], [[34],  [6,2,5]]) == False

def test_case10() :
        assert areIsomorphic.areIsomorphic([[6], [3,5,2,4]], [[34],  [6,2,5,4],  [1,2,3]]) == False
