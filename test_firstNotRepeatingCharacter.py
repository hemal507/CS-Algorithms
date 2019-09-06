import firstNotRepeatingCharacter

def test_case1():
	assert firstNotRepeatingCharacter.firstNotRepeatingCharacter("ababcbaba") == "c"

def test_case2():
	assert firstNotRepeatingCharacter.firstNotRepeatingCharacter("abacabaabacaba") ==  "_"

def test_case3():
	assert firstNotRepeatingCharacter.firstNotRepeatingCharacter("bcccccccb") == "_"

def test_case4():
	firstNotRepeatingCharacter.firstNotRepeatingCharacter("bcb") == 'c'
