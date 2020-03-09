import countVowelConsonant


def test_case1():
    assert countVowelConsonant.countVowelConsonant("a") == 1


def test_case2():
    assert countVowelConsonant.countVowelConsonant("abcde") == 8


def test_case3():
    assert countVowelConsonant.countVowelConsonant("") == 0


def test_case4():
    assert countVowelConsonant.countVowelConsonant("oqaawtnkqo") == 16


def test_case5():
    assert countVowelConsonant.countVowelConsonant("dsnhpbpfkmqbclwy") == 32


def test_case6():
    assert countVowelConsonant.countVowelConsonant("fpwbqfvucwepocdapglyxwnqwlegsqxhxlfkmfaz") == 74


def test_case7():
    assert countVowelConsonant.countVowelConsonant("teilziwavjyjykgccxkdzsalpkvnxoynpfpowgmhfvozwdbems") == 91
