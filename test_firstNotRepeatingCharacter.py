import firstNotRepeatingCharacter


def test_case1():
    assert firstNotRepeatingCharacter.firstNotRepeatingCharacter("ababcbaba") == "c"


def test_case2():
    assert firstNotRepeatingCharacter.firstNotRepeatingCharacter("abacabaabacaba") == "_"


def test_case3():
    assert firstNotRepeatingCharacter.firstNotRepeatingCharacter("z") == "z"


def test_case4():
    assert firstNotRepeatingCharacter.firstNotRepeatingCharacter("bcb") == 'c'


def test_case5():
    assert firstNotRepeatingCharacter.firstNotRepeatingCharacter("bcccccccb") == "_"


def test_case6():
    assert firstNotRepeatingCharacter.firstNotRepeatingCharacter("abcdefghijklmnopqrstuvwxyziflskecznslkjfabe") == "d"


def test_case7():
    assert firstNotRepeatingCharacter.firstNotRepeatingCharacter("zzz") == "_"


def test_case8():
    assert firstNotRepeatingCharacter.firstNotRepeatingCharacter("bcccccccccccccyb") == 'y'


def test_case9():
    assert firstNotRepeatingCharacter.firstNotRepeatingCharacter(
        "xdnxxlvupzuwgigeqjggosgljuhliybkjpibyatofcjbfxwtalc") == "d"


def test_case10():
    assert firstNotRepeatingCharacter.firstNotRepeatingCharacter("ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadl"
																 "tsuxbfbrkof") == 'g'
