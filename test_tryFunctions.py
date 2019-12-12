import tryFunctions

def test_case1() :
	assert tryFunctions.tryFunctions(1, ["math.sin",  "math.cos",  "lambda x: x * 2",  "lambda x: x ** 2"]) == [0.84147, 0.5403, 2, 1]

def test_case2() :
        assert tryFunctions.tryFunctions(-20, ["abs"]) == [20]

def test_case3() :
        assert tryFunctions.tryFunctions(25.5, ["lambda x: int(x)",  "int",  "math.floor"]) == [25, 25, 25]

def test_case4() :
        assert tryFunctions.tryFunctions(3, ["math.factorial",  "math.exp",  "lambda x: 2 ** x"]) == [6, 20.0855369232, 8]

def test_case5() :
        assert tryFunctions.tryFunctions(-1000, ["lambda z: z",  "lambda z: 1.0 * z / 13"]) == [-1000, -76.9230769231]

def test_case61() :
        assert tryFunctions.tryFunctions(1000,  ["float"]) == [1000]
