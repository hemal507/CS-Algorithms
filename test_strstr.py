import strstr

def test_case1() :
	assert strstr.strstr("CodefightsIsAwesome","IA") == -1

def test_case2() :
        assert strstr.strstr("CodefightsIsAwesome","IsA") == 10

def test_case3() :
        assert strstr.strstr("a","a") == 0

def test_case4() :
        assert strstr.strstr("a","A") == -1

def test_case5() :
        assert strstr.strstr("sst","st") == 1

def test_case6() :
        assert strstr.strstr("lrnkbldxguzgcseccinlizyogwqzlifxcthdgmanjztlt","an") == 38

def test_case7() :
        assert strstr.strstr("ffbefbdbacbccecaceddcbcaeaebfedfcfdbeecffdbbf","cb") == 9

def test_case8() :
        assert strstr.strstr("ATErUUeUkVFVNfxfUKtntOErKmZLUpWpHRASdxjUhzzxygmnNnKabPPgPqyvCLSCZObaNNGCXQssfEEDDJIPBwtkMmTniKapBlrd","vCLSCZObaNNGCXQssfEEDDJIPBwtkMmTniKa") == 59

