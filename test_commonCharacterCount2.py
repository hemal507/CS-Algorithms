import commonCharacterCount2


def test_case1():
    assert commonCharacterCount2.commonCharacterCount2(["aabcc", "adcaa", "acdba"]) == 3


def test_case2():
    assert commonCharacterCount2.commonCharacterCount2(["aabcc", "adcaa", "ddddddbbbbbabbd"]) == 1


def test_case3():
    assert commonCharacterCount2.commonCharacterCount2(["aabcc", "adcaa"]) == 3


def test_case4():
    assert commonCharacterCount2.commonCharacterCount2(["zzzz", "zzzzzzz"]) == 4


def test_case5():
    assert commonCharacterCount2.commonCharacterCount2(["zzzz", "yyyyyyy"]) == 0


def test_case6():
    assert commonCharacterCount2.commonCharacterCount2(["abcdefghxyzttw", "hgfedcbaabcwwt"]) == 10


def test_case7():
    assert commonCharacterCount2.commonCharacterCount2(["abcdefabcdef"]) == 12


def test_case8():
    assert commonCharacterCount2.commonCharacterCount2(
        ["afcdbceccfecfafdfbddaebbaadefdeaadfaedefacebfdcadcfafbaabedbfeda",
         "cccabfacfbcfabbfaefeddcecafdffbaafaddfaaecaeeebdebecbbbfedbaafcedaddfecbedfae",
         "dccddbcedccdaeacdfffeacccafafebebdbeaeadeeeaeeaeddbafdfdfaacafceedfcbdcadecdbafafeacadaeeaacaaafb",
         "bcaecaafcdacadaadcfadfccdaffefabaffdfbfffcdeabecdacaecebffcaaebceecacabfeeeddbccd",
         "afcfaacbaceaadadbfedfeccefcebdabaaebbaffacaadbcdaccecbdbdcbcddfeefafebfdfbaf"]) == 63


def test_case9():
    assert commonCharacterCount2.commonCharacterCount2(
        ["kcegkkdfikcfgffhibdejdagiejhchackdiddaeibfjbchfifgkkckdfijdffcejiafgjj",
         "hbehcdbbajkjbedjkjdidkaiichhhaidfhhhkbddgekddde",
         "djbahbcjhkhcdi",
         "badddeajheeccifjiefikihaakhghbcajj",
         "dkcbhbhegkgafgccjkhiadjec"]) == 14


def test_case10():
    assert commonCharacterCount2.commonCharacterCount2(
        ["caedcbdcbecdbfcfbcedadbafbfeefbedaacbceafddfeeadbdaffecbaffaefdeafedfaefacc",
         "ddefeededaecbaadeddacbeddebeaeccbafdcaecaffcfdffecaeeaedefbadabffccbbffebffbaddbcfdaaedfabfaecc",
         "cfbacfcffbaeccefdedeaffbcdadbdfcaeebdafffbaeefcabecabcfddceefebceb",
         "eafeddfbcfcbfcbfceefeebefdfbdafffeecfacbbaadfbbcdccaaaeeeebdcabd",
         "eaebcffbffacdefefebfbeaaacceaedfbbdcccfddebdedafdeeacabbecbfffcfdca",
         "afeecdcebaedfeabfdafcabbdcacfdfaaaaefbffaceaffaecfebdccffbaecbfbccddcbdbcbbeecfceee",
         "abeeefcdfbacedacecdeaafbbfbfffeecabdbafdfdfabcabefcfedcdcebcefedf",
         "feeadefaeebfdbfbcdfdaaaaaffdbbddbcebcefdedcfcaccdfaffbcfecbdabffcedeceaeefcaffdeeecfafbb",
         "bdffafbcfbbbefbccdcfcdceeceddcfdedffaabfefecbeffcaceebdaeacebdefadafaecaffeabdebcad",
         "eabcaafbfcaabeaacecfabbfcecdddbdedfdefdbfeddcbbfcbfdceefbcaefaaeeffdeefabffcaccaceafc"]) == 63


def test_case11():
    assert commonCharacterCount2.commonCharacterCount2(
        ["dcuceeizkgnrqmacwanczkjmbrkxwvtoddgshqigwzpqtwzjudhjmrqxdkrpbxkasggvyphbsvtjajwsccinrznvncusitucqug",
         "ardqxukrdagkqgmbcsgviiibremjdrwushudvythvjldtzezgnqmcnscxgchwvutdeggxwpcnrnqxspzckjwuewrcsajitvekqt",
         "drpecxnwutxavncgimcvrgkjuqgdhbxrnwqtrzkmzievqcrwsajqugqzatthrsucydijwgscxcsjdwkpsmkhnvg",
         "qhsaiuqcgtmqpmmdtwxsvgenwkiigevvthyvrgjswkrwaexjazcquszjdvtcbcndugkdwsznyridzsrguenwjwcopchurqkmecx",
         "cgwnuvkmnrsynuguekddqtpmeyrhzgjzisgzwcvcsriadiqvrawgccmmkyvtksxqcxrjzwqtghgqbhtdvknxopckhwmjjasudu"]) == 85
