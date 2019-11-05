import capitalizeVowelsRegExp

def test_case1():
	assert capitalizeVowelsRegExp.capitalizeVowelsRegExp("There are 12 points") == "ThErE ArE 12 pOInts"

def test_case2():
	assert capitalizeVowelsRegExp.capitalizeVowelsRegExp(" _Aaaaas 23") == " _AAAAAs 23"

def test_case3():
	assert capitalizeVowelsRegExp.capitalizeVowelsRegExp(" a_2") == " A_2"
