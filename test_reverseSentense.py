import reverseSentence


def test_case1():
    assert reverseSentence.reverseSentence("Man bites dog") == "dog bites Man"


def test_case2():
    assert reverseSentence.reverseSentence("IHateSpaces") == "IHateSpaces"


def test_case3():
    assert reverseSentence.reverseSentence("a b c") == "c b a"


def test_case4():
    assert reverseSentence.reverseSentence("BgwlaMUMkToumKe ANHz") == "ANHz BgwlaMUMkToumKe"
