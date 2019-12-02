import longestWord

def test_case1():
	assert longestWord.longestWord("Ready, steady, go!") == "steady"

def test_case2():
        assert longestWord.longestWord("Ready[[[, steady, go!") == "steady"

def test_case3():
        assert longestWord.longestWord("ABCd") == "ABCd"

def test_case4():
        assert longestWord.longestWord("To be or not to be") == "not"

def test_case5():
        assert longestWord.longestWord("You are the best!!!!!!!!!!!! CodeFighter ever!") == "CodeFighter"
