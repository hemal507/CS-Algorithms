import stolenLunch

def test_case1() :
	assert stolenLunch.stolenLunch("you'll n4v4r 6u4ss 8t: cdja") == "you'll never guess it: 2390"

def test_case2() :
        assert stolenLunch.stolenLunch("") == ""

def test_case3() :
        assert stolenLunch.stolenLunch("0123456789") == "abcdefghij"

def test_case4() :
        assert stolenLunch.stolenLunch("jihgfedcba") == "9876543210"

def test_case5() :
        assert stolenLunch.stolenLunch("you won't know!!") == "you won't know!!"

def test_case6() :
        assert stolenLunch.stolenLunch( "just 63jd73 some random note jkhdf83 ds823 that you, dfj238 dsf38 little one?, will abjk38 s83    skdu3 29never get!") == "9ust gd93hd som4 r0n3om not4 9k735id 3sicd t70t you, 359cdi 3s5di l8ttl4 on4?, w8ll 019kdi sid    sk3ud cjn4v4r 64t!"
