import addBorder

def test_case1() :
	assert addBorder.addBorder(["abc",  "ded"]) == ["*****",  "*abc*",  "*ded*",  "*****"]

def test_case2() :
        assert addBorder.addBorder(["a"]) == ["***",  "*a*",  "***"]

def test_case3() :
        assert addBorder.addBorder(["aa",  "**",  "zz"]) == ["****",  "*aa*",  "****",  "*zz*",  "****"]

def test_case4() :
        assert addBorder.addBorder(["abcde",  "fghij",  "klmno",  "pqrst",  "uvwxy"]) == ["*******",  "*abcde*",  "*fghij*",  "*klmno*",  "*pqrst*",  "*uvwxy*",  "*******"]

def test_case5() :
        assert addBorder.addBorder(["wzy**"]) == ["*******",  "*wzy***",  "*******"]

