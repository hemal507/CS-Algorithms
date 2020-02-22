import stringPermutations


def test_case1():
    assert stringPermutations.stringPermutations("CBA") == ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]


def test_case2():
    assert stringPermutations.stringPermutations("ABA") == ["AAB", "ABA", "BAA"]


def test_case3():
    assert stringPermutations.stringPermutations("ABSG") == ["ABGS", "ABSG", "AGBS", "AGSB", "ASBG", "ASGB", "BAGS",
                                                             "BASG", "BGAS", "BGSA", "BSAG", "BSGA", "GABS", "GASB",
                                                             "GBAS", "GBSA", "GSAB", "GSBA", "SABG", "SAGB", "SBAG",
                                                             "SBGA", "SGAB", "SGBA"]


def test_case4():
    assert stringPermutations.stringPermutations("AE") == ["AE", "EA"]


def test_case5():
    assert stringPermutations.stringPermutations("SABHD") == ["ABDHS", "ABDSH", "ABHDS", "ABHSD", "ABSDH", "ABSHD",
                                                              "ADBHS", "ADBSH", "ADHBS", "ADHSB", "ADSBH", "ADSHB",
                                                              "AHBDS", "AHBSD", "AHDBS", "AHDSB", "AHSBD", "AHSDB",
                                                              "ASBDH", "ASBHD", "ASDBH", "ASDHB", "ASHBD", "ASHDB",
                                                              "BADHS", "BADSH", "BAHDS", "BAHSD", "BASDH", "BASHD",
                                                              "BDAHS", "BDASH", "BDHAS", "BDHSA", "BDSAH", "BDSHA",
                                                              "BHADS", "BHASD", "BHDAS", "BHDSA", "BHSAD", "BHSDA",
                                                              "BSADH", "BSAHD", "BSDAH", "BSDHA", "BSHAD", "BSHDA",
                                                              "DABHS", "DABSH", "DAHBS", "DAHSB", "DASBH", "DASHB",
                                                              "DBAHS", "DBASH", "DBHAS", "DBHSA", "DBSAH", "DBSHA",
                                                              "DHABS", "DHASB", "DHBAS", "DHBSA", "DHSAB",
                                                              "DHSBA", "DSABH", "DSAHB", "DSBAH", "DSBHA", "DSHAB",
                                                              "DSHBA", "HABDS", "HABSD", "HADBS", "HADSB", "HASBD",
                                                              "HASDB", "HBADS", "HBASD", "HBDAS", "HBDSA", "HBSAD",
                                                              "HBSDA", "HDABS", "HDASB", "HDBAS", "HDBSA", "HDSAB",
                                                              "HDSBA", "HSABD", "HSADB", "HSBAD", "HSBDA", "HSDAB",
                                                              "HSDBA", "SABDH", "SABHD", "SADBH", "SADHB", "SAHBD",
                                                              "SAHDB", "SBADH", "SBAHD", "SBDAH", "SBDHA", "SBHAD",
                                                              "SBHDA", "SDABH", "SDAHB", "SDBAH", "SDBHA", "SDHAB",
                                                              "SDHBA", "SHABD", "SHADB", "SHBAD", "SHBDA", "SHDAB",
                                                              "SHDBA"]
