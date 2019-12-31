import functionsComposition

def test_case1() :
	assert functionsComposition.functionsComposition(["abs",  "math.sin",  "lambda x: 3 * x / 2"], 3.1415) == 0.9999999903422263

def test_case2() :
        assert functionsComposition.functionsComposition(["math.sin",  "math.cos",  "lambda x: x * 2",  "lambda x: x ** 2"], 1) == -0.4042391538522658

def test_case3() :
        assert functionsComposition.functionsComposition(["lambda z: z",  "lambda z: 1.0 * z / 13"], -1000) == -76.92307692307692

def test_case4() :
        assert functionsComposition.functionsComposition(["float"], 1000) == 1000

def test_case5() :
        assert functionsComposition.functionsComposition(["abs"], -20) == 20
