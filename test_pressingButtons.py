import pressingButtons


def test_case1():
    assert pressingButtons.pressingButtons("42") == ['ga', 'gb', 'gc', 'ha', 'hb', 'hc', 'ia', 'ib', 'ic']


def test_case2():
    assert pressingButtons.pressingButtons("2") == ["a", "b", "c"]


def test_case3():
    assert pressingButtons.pressingButtons("3") == ["d", "e", "f"]


def test_case4():
    assert pressingButtons.pressingButtons("") == []


def test_case5():
    assert pressingButtons.pressingButtons("234") == ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi',
                                                      'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi',
                                                      'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']


def test_case6():
    assert pressingButtons.pressingButtons("8888") == ['tttt', 'tttu', 'tttv', 'ttut', 'ttuu', 'ttuv', 'ttvt', 'ttvu',
                                                       'ttvv', 'tutt', 'tutu', 'tutv', 'tuut', 'tuuu', 'tuuv', 'tuvt',
                                                       'tuvu', 'tuvv', 'tvtt', 'tvtu', 'tvtv', 'tvut', 'tvuu', 'tvuv',
                                                       'tvvt', 'tvvu', 'tvvv', 'uttt', 'uttu', 'uttv', 'utut', 'utuu',
                                                       'utuv', 'utvt', 'utvu', 'utvv', 'uutt', 'uutu', 'uutv', 'uuut',
                                                       'uuuu', 'uuuv', 'uuvt', 'uuvu', 'uuvv', 'uvtt', 'uvtu', 'uvtv',
                                                       'uvut', 'uvuu', 'uvuv', 'uvvt', 'uvvu', 'uvvv', 'vttt', 'vttu',
                                                       'vttv', 'vtut', 'vtuu', 'vtuv', 'vtvt', 'vtvu', 'vtvv', 'vutt',
                                                       'vutu', 'vutv', 'vuut', 'vuuu', 'vuuv', 'vuvt', 'vuvu', 'vuvv',
                                                       'vvtt', 'vvtu', 'vvtv', 'vvut', 'vvuu', 'vvuv', 'vvvt', 'vvvu',
                                                       'vvvv']
