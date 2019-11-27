import checkPalindrome

def test_case1() :
	assert checkPalindrome.checkPalindrome("aabaa") == True

def test_case2() :
        assert checkPalindrome.checkPalindrome("abac") == False

def test_case3() :
        assert checkPalindrome.checkPalindrome("a") == True

def test_case4() :
        assert checkPalindrome.checkPalindrome("az") == False

def test_case5() :
        assert checkPalindrome.checkPalindrome("abacaba") == True

def test_case6() :
        assert checkPalindrome.checkPalindrome("hlbeeykoqqqqokyeeblh") == True

