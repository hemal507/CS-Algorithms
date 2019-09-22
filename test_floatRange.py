import floatRange

def test_case1() :
	assert [round(x,2) for x in floatRange.floatRange(-0.9,0.45,0.2)] == [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3]

def test_case2() :
        assert [round(x,2) for x in floatRange.floatRange(1.5,1.5,10) ]  == []

def test_case3() :
        assert [round(x,2) for x in floatRange.floatRange(1,2,1.5)] == [1]

def test_case4() :
        assert [round(x,2) for x in floatRange.floatRange(-21.11,21.11,1.11) ] == [-21.11, -20, -18.89, -17.78, -16.67, -15.56, -14.45, -13.34, -12.23, -11.12, -10.01, -8.9, -7.79, -6.68, -5.57, -4.46, -3.35, -2.24, -1.13, -0.02, 1.09, 2.2, 3.31, 4.42, 5.53, 6.64, 7.75, 8.86, 9.97, 11.08, 12.19, 13.3, 14.41, 15.52, 16.63, 17.74, 18.85, 19.96, 21.07]

def test_case5() :
        assert [round(x,2) for x in floatRange.floatRange(0,1,0.05) ] == [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
