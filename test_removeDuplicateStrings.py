import removeDuplicateStrings

def test_case1() :
	assert removeDuplicateStrings.removeDuplicateStrings(["a",  "a",  "ab",  "ab",  "abc"]) == ["a",  "ab",  "abc"]

def test_case2() :
        assert removeDuplicateStrings.removeDuplicateStrings(["a",  "a",  "a"]) == ["a"]

def test_case3() :
        assert removeDuplicateStrings.removeDuplicateStrings(["123",  "12345",  "12324345"]) == ["123",  "12345",  "12324345"]


