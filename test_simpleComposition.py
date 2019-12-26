import simpleComposition

def test_case1() :
	assert simpleComposition.simpleComposition("math.sin","math.cos",34.4) == -0.8347174456642033

def test_case2() :
        assert simpleComposition.simpleComposition("math.log10","abs",-100) == 2

def test_case3() :
        assert simpleComposition.simpleComposition("int","lambda x: 1.0 * x / 22",1000) == 45

def test_case4() :
        assert simpleComposition.simpleComposition("math.exp","lambda x: x ** 0", -1000) == 2.718281828459045

def test_case5() :
        assert simpleComposition.simpleComposition("lambda z: z","lambda y: y",239) == 239


