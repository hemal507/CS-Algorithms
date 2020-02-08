import rockPaperScissors


def test_case1():
    assert all([list(a) in [["ninja", "trainee"],
                            ["ninja", "warrior"],
                            ["trainee", "ninja"],
                            ["trainee", "warrior"],
                            ["warrior", "ninja"],
                            ["warrior", "trainee"]] for a in rockPaperScissors.rockPaperScissors(["trainee",
                                                                                                  "warrior",
                                                                                                  "ninja"])])


def test_case2():
    assert all([list(a) in [["hero", "macho"],
                            ["macho", "hero"]] for a in rockPaperScissors.rockPaperScissors(["macho",
                                                                                             "hero"])])


def test_case3():
    assert all([list(a) in [["I", "Novice player with promising future"],
                            ["I", "Player"],
                            ["I", "Professional player of great experience"],
                            ["I", "You"],
                            ["Novice player with promising future", "I"],
                            ["Novice player with promising future", "Player"],
                            ["Novice player with promising future",
                             "Professional player of great experience"],
                            ["Novice player with promising future", "You"],
                            ["Player", "I"],
                            ["Player", "Novice player with promising future"],
                            ["Player", "Professional player of great experience"],
                            ["Player", "You"],
                            ["Professional player of great experience", "I"],
                            ["Professional player of great experience",
                             "Novice player with promising future"],
                            ["Professional player of great experience", "Player"],
                            ["Professional player of great experience", "You"],
                            ["You", "I"],
                            ["You", "Novice player with promising future"],
                            ["You", "Player"],
                            ["You", "Professional player of great experience"]] for a in
                rockPaperScissors.rockPaperScissors(["Professional player of great experience",
                                                     "Novice player with promising future",
                                                     "You",
                                                     "Player",
                                                     "I"])])


def test_case4():
    assert all([list(a) in [["Draco", "Harry"],
                            ["Draco", "Hermione"],
                            ["Draco", "Ron"],
                            ["Draco", "Tom"],
                            ["Harry", "Draco"],
                            ["Harry", "Hermione"],
                            ["Harry", "Ron"],
                            ["Harry", "Tom"],
                            ["Hermione", "Draco"],
                            ["Hermione", "Harry"],
                            ["Hermione", "Ron"],
                            ["Hermione", "Tom"],
                            ["Ron", "Draco"],
                            ["Ron", "Harry"],
                            ["Ron", "Hermione"],
                            ["Ron", "Tom"],
                            ["Tom", "Draco"],
                            ["Tom", "Harry"],
                            ["Tom", "Hermione"],
                            ["Tom", "Ron"]] for a in rockPaperScissors.rockPaperScissors(["Harry",
                                                                                          "Ron",
                                                                                          "Hermione",
                                                                                          "Draco",
                                                                                          "Tom"])])


def test_case5():
    assert all([list(a) in [["Anakin", "Leia"],
                            ["Anakin", "Luke"],
                            ["Anakin", "Padme"],
                            ["Anakin", "Rey"],
                            ["Leia", "Anakin"],
                            ["Leia", "Luke"],
                            ["Leia", "Padme"],
                            ["Leia", "Rey"],
                            ["Luke", "Anakin"],
                            ["Luke", "Leia"],
                            ["Luke", "Padme"],
                            ["Luke", "Rey"],
                            ["Padme", "Anakin"],
                            ["Padme", "Leia"],
                            ["Padme", "Luke"],
                            ["Padme", "Rey"],
                            ["Rey", "Anakin"],
                            ["Rey", "Leia"],
                            ["Rey", "Luke"],
                            ["Rey", "Padme"]] for a in rockPaperScissors.rockPaperScissors(["Luke",
                                                                                            "Leia",
                                                                                            "Padme",
                                                                                            "Anakin",
                                                                                            "Rey"])])


def test_case6():
    assert all([list(a) in [["A", "B"],
                            ["B", "A"]] for a in rockPaperScissors.rockPaperScissors(["A",
                                                                                     "B"])])
