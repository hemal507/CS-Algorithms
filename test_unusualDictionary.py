import unusualDictionary


def test_case1():
    assert unusualDictionary.unusualDictionary(
        ["the cat", "to hiss", "a kitten", "to meow", "playful", "to purr"]) == True


def test_case2():
    assert unusualDictionary.unusualDictionary(["to desert", "the desert", "a dessert"]) == False


def test_case3():
    assert unusualDictionary.unusualDictionary(["a a", "the", "the the", "to the"]) == True


def test_case4():
    assert unusualDictionary.unusualDictionary(["an", "a a", "b", "c", "d"]) == False


def test_case5():
    assert unusualDictionary.unusualDictionary(["a", "an a", "to a", "a b", "b", "to b"]) == True


def test_case6():
    assert unusualDictionary.unusualDictionary(["a thef", "the thee", "an theee"]) == False


def test_case7():
    assert unusualDictionary.unusualDictionary(["z", "a zoo", "to zoom", "the zoomlion"]) == True


def test_case8():
    assert unusualDictionary.unusualDictionary(["zaa", "a boo", "to oppm", "the oppm"]) == False


def test_case9():
    assert unusualDictionary.unusualDictionary(["the", "the the", "to the", "an to", "to", "to to"]) == True


def test_case10():
    assert unusualDictionary.unusualDictionary(
        ["the abcdefghijklmnopqrstuvwxyz", "an abcdefghijklmnopqrstuvwxyz"]) == False
