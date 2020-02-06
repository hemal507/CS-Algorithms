import transposeDictionary


def test_case1():
    assert transposeDictionary.transposeDictionary({
        "validate": "py",
        "getLimits": "md",
        "generateOutputs": "json"
    }) == [["json", "generateOutputs"],
           ["md", "getLimits"],
           ["py", "validate"]]


def test_case2():
    assert transposeDictionary.transposeDictionary({
        "styleChecker": "cpp",
        "autoBugfixes": "py"
    }) == [["cpp", "styleChecker"],
           ["py", "autoBugfixes"]]


def test_case3():
    assert transposeDictionary.transposeDictionary({}) == []


def test_case4():
    assert transposeDictionary.transposeDictionary({
        "generateTests": "json"
    }) == [["json", "generateTests"]]


def test_case5():
    assert transposeDictionary.transposeDictionary({
        "runSolutions": "validate",
        "generateTests": "generateOutputs",
        "validate": "runSolutions",
        "generatePeh": "generateMeh",
        "generateMeh": "generatePeh",
        "generateOutputs": "generateTests"
    }) == [["generateMeh", "generatePeh"],
           ["generateOutputs", "generateTests"],
           ["generatePeh", "generateMeh"],
           ["generateTests", "generateOutputs"],
           ["runSolutions", "validate"],
           ["validate", "runSolutions"]]
