from DynamicProgramming import editDistance

def test_case1():
    assert editDistance.editDistance("cart","match") == 4

def test_case2():
    assert editDistance.editDistance("cart","cart") == 0

def test_case3():
    assert editDistance.editDistance("a","") == 1

def test_case4():
    assert editDistance.editDistance("","a") == 1

def test_case5():
    assert editDistance.editDistance("CART","cart") == 4

