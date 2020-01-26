import classifyStrings


def test_case1():
    assert classifyStrings.classifyStrings("aeu") == "bad"


def test_case2():
    assert classifyStrings.classifyStrings("a?u") == "mixed"


def test_case3():
    assert classifyStrings.classifyStrings("aba") == "good"


def test_case4():
    assert classifyStrings.classifyStrings("qwrtl") == "bad"


def test_case5():
    assert classifyStrings.classifyStrings("qwr?l") == "mixed"


def test_case6():
    assert classifyStrings.classifyStrings("???") == "mixed"


def test_case7():
    assert classifyStrings.classifyStrings("?") == "good"


def test_case8():
    assert classifyStrings.classifyStrings("?io") == "mixed"


def test_case9():
    assert classifyStrings.classifyStrings("?ypsd") == "mixed"


def test_case10():
    assert classifyStrings.classifyStrings("typ?asdf?relkhfd") == "bad"


def test_case11():
    assert classifyStrings.classifyStrings("lrsesknaiotmqanvt") == "bad"
