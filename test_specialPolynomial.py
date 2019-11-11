import specialPolynomial

def test_case1():
	assert specialPolynomial.specialPolynomial(2,5) == 1

def test_case2() :
	assert specialPolynomial.specialPolynomial(10,111111110) == 7 

def test_case3() :
        assert specialPolynomial.specialPolynomial(1,100) == 99

def test_case4() :
        assert specialPolynomial.specialPolynomial(3,140) == 4
