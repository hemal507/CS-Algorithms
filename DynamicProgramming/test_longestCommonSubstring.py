from DynamicProgramming import longestCommonSubstring


def test_case1():
    assert longestCommonSubstring.longestCommonSubstringDP("abcdxyz", "xyzabcd") == 4


def test_case2():
    assert longestCommonSubstring.longestCommonSubstringDP("zxabcdezy", "yzabcdezx") == 6


def test_case3():
    assert longestCommonSubstring.longestCommonSubstringDP("ABC", "ABCD") == 3


def test_case4():
    assert longestCommonSubstring.longestCommonSubstringDP("ABCD", "ABC") == 3


def test_case5():
    assert longestCommonSubstring.longestCommonSubstringDP("ABCDGH", "ACDGHR") == 4


def test_case6():
    assert longestCommonSubstring.longestCommonSubstringDP("ABC", "AC") == 1


def test_case7():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "LRBBMQBHCDARZOWKKYHIDDQSCDXRJMOWFRXSJYBLDBEFSARCBYNECDYGGXXPKLORELLNMPAPQFWKHOPKMCO",
        "QHNWNKUEWHSQMGBBUQCLJJIVSWMDKQTBXIXMVTRRBLJPTNSNFWZQFJMAFADRRWSOFSBCNUVQHFFBSAQXWPQCAC") == 2


def test_case8():
    assert longestCommonSubstring.longestCommonSubstringDP("CHZVFRKMLNOZJK",
                                                           "PQPXRJXKITZYXACBHHKICQCOENDTOMFGDWDWFCGPXIQVKUYTDLCGDEWHTACIOHORDTQKVWCSGSPQOQMSBOAGUWN") == 1


def test_case9():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "QXNZLGDGWPBTRWBLNSADEUGUUMOQCDRUBETOKYXHOACHWDVMXXRDRYXLMNDQTUKWAGMLEJUUKWCIBXU",
        "BUMENMEYATDRMYDIAJXLOGHIQFMZHLVIHJOUVSUYOYPAYULYEI") == 2


def test_case10():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "OTEHZRIICFSKPGGKBBIPZZRZUCXAMLUDFYKGRUOWZGIOOOBPPLEQLWPHAPJNADQHDCNVWDTXJBMYPPPHAUXNSPUSGDHIIXQMBF",
        "JXJCVUDJSUYIBYEBMWSIQYOYGYXYMZEVYPZV") == 2


def test_case11():
    assert longestCommonSubstring.longestCommonSubstringDP("GEBEOCFUFTSXDIXTIGSIEEHKCHZ", "DFLILRJQFNXZ") == 1


def test_case12():
    assert longestCommonSubstring.longestCommonSubstringDP("RSVBSPK",
                                                           "YHSENBPPKQTPDDBUOTBBQCWIVRFXJUJJDDNTGEIQVDGAIJVWCYAUBWEWPJVYGEHLJXEPBPIWUQZDZU") == 2


def test_case13():
    assert longestCommonSubstring.longestCommonSubstringDP("UBZVAFSPQPQ", "WUZIF") == 1


def test_case14():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "VYDDWYVVBURCZMGYJGFDXVTNUNNESLSPLWUIUPFXLZBKNHKWPPANLTCFIRJCDDSOZOYVEGURFW", "CSFMOXEQMRJOWRGHWLKOBMEAHK") == 2


def test_case15():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "CNAEHHSVEYMQPXHLRNUNYFDZRHBASJEUYGAFOUBUTPNIMUWFJQSJXVKQDORXXVRWCTDSNEOGVBPKXLPGDIRBFC",
        "RIQIFPGYNKRREFXSNVUCFTPWCTGTWMXNUPYCFGCU") == 3


def test_case16():
    assert longestCommonSubstring.longestCommonSubstringDP("NUBLMOIITNCKLEFSZBEX",
                                                           "RAMPETVHQNDDJEQVUYGPNKAZQFRPJVOAXDPCWMJOBMSKSKFOJNEWXGXNNOFWLTWJWNNVBWJCKDMEOUUZHYVHGVWUJBQX") == 2


def test_case17():
    assert longestCommonSubstring.longestCommonSubstringDP("ITCVOGRAIDDVHRRDSYCQHKLEEWHXTEMBAQWQW",
                                                           "PQHSUEBNVFGVJWDVJJAFQZZXLCXDZNCQGJLAPOPKVXFGVICETCMKBLJOPGT") == 2


def test_case18():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "VHBGSDVIVHESNKQXMWRQIDRVMHLUBBRYKTHEYENTMROBDEYQCRGLUAIIHVEIXWJJRQOPUBJGUXHX",
        "DIPFZWSWYBGFYLQVJZHARVRLYAUUZDRCNJKPHCLFFRKEECBPDIPUFHIDJCXJHRNXCXMJCXOHQANXDRMGZEB") == 2


def test_case19():
    assert longestCommonSubstring.longestCommonSubstringDP("LMWPMHWDVTHSFQUEEEXGRUJIGSKMVRZGFWVRFTWAPDT",
                                                           "UTPBZTYGNSRXAJJNGCOMIKJZSDWSSZNOVDRUYPCNJULKFUZMXNAFAMESPCKJCAZXDRTDGYRQSCCZYBN") == 2


def test_case20():
    assert longestCommonSubstring.longestCommonSubstringDP("QCQCJITLVCNVBMASIDZ",
                                                           "GWRAATZZWPWMFBFJKNCVKELHHZJCHPDNLUNMPPNLGJZNKEWWUYSGEFONEXPM") == 1


def test_case21():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "BAOPMDGZQMKQZXUVTQVNXBSLQZKGLZAMZPDNSJOLVYBWXXTTQOGNRBAIAKQLLSZKHF",
        "ZCONNMOQKLPEEFSNSMOUWQHODSGCFOHESYSHMGXWTOAYUVNOJDJFTQTWKBAPRIUJIMQWSPSLGVLCSAQBDBGWTBSEETTWDNFNBY") == 2


def test_case22():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "PDJXYUZQXSTATBZPCTTHOOFREMGFKRBCVKZVGBOFTHGOJHDNAYWPNBITORAAIBEDNEZWFPDAWLOHSSVTQ", "TKFVSYLJZLUCQ") == 1


def test_case23():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "WYQDNTDMFRTZLQSEKEJHZKSKLFEPXCHVCZYSVDGCXBBISWMEAYLZIFKTMOIKSSFXTGPOJXQIYSRSQFWQDJQNQCGDQRNLLUI",
        "EAZVMWNUUFNNXVLOYVGMLIUQANDLYAVFAUAOSNLNVACSVPIUMOIAWCQXSWKQWGXYAZNTNAIKAMEYBNUQBCQAGGXACHRYNQXQQM") == 3


def test_case24():
    assert longestCommonSubstring.longestCommonSubstringDP("OTPQHVOKIIAMMQMVXJVBSOA",
                                                           "IFZYXNJCBERRNMIXXSYJHOVENGBPYQRIXQGWDRYGXRXKFHICAINHWILKQMBPESZDIGZNZ") == 2


def test_case25():
    assert longestCommonSubstring.longestCommonSubstringDP("ZQSJWATYCBMJAWWMNINEPFDUPLUCLTXMKPV",
                                                           "GRRGTUSEURAGELTKCAPWPBQROMQAWIX") == 2


def test_case26():
    assert longestCommonSubstring.longestCommonSubstringDP("QKVLFBHWCOCPJMRMBPBEGVSULUQTUUVKESVJTDHVTJMEXFQBVUFDPAXCWN",
                                                           "WQJTBPLYZEDICWSODPWTQRPYUEARHWGFNPAQELOFRSOTQIKTXIPQZ") == 2


def test_case27():
    assert longestCommonSubstring.longestCommonSubstringDP("VLQMUOUBBJBRPMIXFCLBSTNOSVDKUJCPWSDQHXRKIUEZIO",
                                                           "WOQJPIECWXXBJTNMKJGNCPMVAUQGTAUSOKBFUGJTFIUQBJCLVLAZAMUCIMICNEWDOX") == 2


def test_case28():
    assert longestCommonSubstring.longestCommonSubstringDP("FUEMDADGKHUFSUEVJAXRNIVCORHFRQQWNUJQU", "O") == 1


def test_case29():
    assert longestCommonSubstring.longestCommonSubstringDP("VSLQPRLYSKRHUNLJGSOXLEUYYFQU",
                                                           "TOZQHMGYETYYEPFAESJLKZIVDEVDLLYGAZXJNDJRXHRDYYDDQNQDOAYSHWXSHXZJYWUMBFFAMXDNXJQOYIRMIR") == 2


def test_case30():
    assert longestCommonSubstring.longestCommonSubstringDP("NEKXDLICJFQKKVNXUQMSZCIXMZKWSQOIWYFALP",
                                                           "EUUUGFRTEOMQINUQNIRXELP") == 2


def test_case31():
    assert longestCommonSubstring.longestCommonSubstringDP("OSAODQSZKOGRFBXTNPDBLTQTMPYYEQTUJUIOKCOWSWQYXN",
                                                           "TNDXQQSGKHVIHBAAWJUGAGLODDKTDJIZYNYOESU") == 2


def test_case32():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "RYITYJRIFXIMKYROKKTVUSUIQIOJFCKYATRYEKIJKSVUSOKCYEAVWUFPCTAJXKIXDBXJMITWCQQX",
        "FBBFHBADVFUAAUJXFRWKVUUHEPDIFVFKYHSFIULEA") == 2


def test_case33():
    assert longestCommonSubstring.longestCommonSubstringDP("AAPAHJWTESPLWEQFMNMYMTQ", "RELEIN") == 1


def test_case34():
    assert longestCommonSubstring.longestCommonSubstringDP("PMFPVOMQUEGHDMXKYNWXZQNSWAXGNJWDXBUUSGKMNQWQDVADIW",
                                                           "AHOQAKQZQGKMLHQFDIMNWZGSPLOROWNPGEHIOXHHFRVQALWDTKSSLY") == 3


def test_case35():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "JATAXGPDMYLDXUKDNFTPRRUMBMEMLROWRHWOQNTCLGHLCRORZHGSBAECPLPCCDYVNXMDMFHAOPLQ",
        "IZKHIQBJTIMITDKXIKSXJECWMKWABHSL") == 2


def test_case36():
    assert longestCommonSubstring.longestCommonSubstringDP("VQVWCQEQAZTKYDWRBGXDCJPALSHGEPKZHHVLXCBXDWJCCGTDOQIS",
                                                           "CYSPQZVUQIVZPTLPVOOYNYAPGVSWOAOSAGHRFFNXNJYEELTZAIZNIC") == 2


def test_case37():
    assert longestCommonSubstring.longestCommonSubstringDP("ZWKNWYHZGPQLWFKJQIPUUJVWTXLBZNRYJDOHBVGHMYUIGGTYQJTMUQ",
                                                           "INNTQMIHNTKDDNALWNMSXSATQQELDACNNPJFERMRNYUQNWBJJPDJHDEAVKNYKPOXHX") == 2


def test_case38():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "QQEDQAVDWZOIORRWWXYRHLSRDGQKDUVTMZZCZUFVTVFIOYGKVEDERVVUDNEGHB",
        "CTCBXDXEZRZGBPFHZANFFECCBGQFMZJQTLRSPPXQIYWJOBSPEFUJLXNMDDURDDIYOBQ") == 2


def test_case39():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "PVCOULCVDRZKMKWLYIQDCHGHRGYTZDNOBQCVDEQJYSTMEPXCANIEWQMOXKJWPYMQORLUXEDVYWHCOGH", "OT") == 1


def test_case40():
    assert longestCommonSubstring.longestCommonSubstringDP("SFGIESTCKRPAIGOCFUFBUBIYRRFFMWAEEIMIDFNNZCPHKFL", "PB") == 1


def test_case41():
    assert longestCommonSubstring.longestCommonSubstringDP("VTDWLUDS",
                                                           "GAUNGFZOIHBXIFOPRWCJZSDXNGTACWTJYPWEUXVEGYBOGSFXQHIP") == 1


def test_case42():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "MPUFPXCKICAGHUFCZMACCGWIGMRQCTEQKBWBAAMICOQLIVNJJOOMWKUCZNVDGZTQA", "RSARGKWUAHEYVOHLETJQPO") == 1


def test_case43():
    assert longestCommonSubstring.longestCommonSubstringDP("JSLKOELFYNZEAVAACEAZUIMYDYPVMGYXBLHPPUUNK",
                                                           "TTKQTMVANUUVJVAHMVVUV") == 2


def test_case44():
    assert longestCommonSubstring.longestCommonSubstringDP("HZKYWHMGCHQVDCQDPMZMXWNEIKZFGTANTNLPWZ",
                                                           "VAHNVKPLPFAOTXNGEXRFCZZDMUSZLOBIOKVKWKXLRXBLVOTZOMEQLFTXZLZKBCSQMNCIAZVRZYEUPYVDKBTWHPVGCWTEYLWKB") == 2


def test_case45():
    assert longestCommonSubstring.longestCommonSubstringDP("BXRUWSZSHXPM",
                                                           "JRHFAWDIBZBFYPDKSBHTAAPZSORBNJPZCXECVJMWJQDJHGVZJCUKFJJZACBPNSOPPVTLEI") == 2


def test_case46():
    assert longestCommonSubstring.longestCommonSubstringDP("YNYFVUEFYYRDJADJEGBSY",
                                                           "PJOMFBRNKILZHSVBWCZWTDFVIRBOSVMJFCYMDRZQZKPGEMJAOJYJOFEYWIMQDAC") == 2


def test_case47():
    assert longestCommonSubstring.longestCommonSubstringDP("AWITXYSJQZNCIPTTNC", "JTJHRTVKW") == 1


def test_case48():
    assert longestCommonSubstring.longestCommonSubstringDP("JBQHJJFKBOACCENRXIHCSANBTGXDCTTNUJVFSCRWQTYUYNMXWVBQXORQ",
                                                           "UOWZHPMDZJLR") == 1


def test_case49():
    assert longestCommonSubstring.longestCommonSubstringDP("NCYOYWBMVZHXPENHVIVTHFIVKHFXBQAQUYETWIFTHNSXRGGOQBHXIQSVZ",
                                                           "ZSCQUTMSZF") == 2


def test_case50():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "NMTAEQTMYKCBRZKJUHLTZNLUIYOKFHVSTOUZGQMEAOGRQSDMZOHYDTUOTJYYST", "TLKNMQDYVDPBX") == 2


def test_case51():
    assert longestCommonSubstring.longestCommonSubstringDP(
        "ATUQASTVPHOAHPSDIFNXRFBQAGHDFOYHHSXHNTDCCTCMIUPQZEQSJRKMZRPHFOOOIOYVJDXNWBZHVQZWUPRGIBSITJPAZFRIT",
        "PFESFSQGR") == 1


def test_case52():
    assert longestCommonSubstring.longestCommonSubstringDP("KXCGMTMVVGFQQWSPD",
                                                           "JXZADDUKVLQPKUZJZHWSUTPCAFSYAIBJHAMMEGWBTPQELRNKBLDXGUZGCSEC") == 2


def test_case53():
    assert longestCommonSubstring.longestCommonSubstringDP("NLIZYOGWQZLIFXCTHDGMANJZTLTANVIAJSCHHKDXLRFROHMXMSMMHVODIH",
                                                           "DVFNXOFBXMLCLXVROJACJPWXBEURHCBMZGZWWGYVTLZEIVXYGAAPPZOSDIKKMLWLTXIRDIOYTNFEIEEPEH") == 2


def test_case54():
    assert longestCommonSubstring.longestCommonSubstringDP("GVQJFAVSNTFIQNBVXPUTCZZNFDCMKKHSHXDNZYHORMWJ",
                                                           "CXFBOBWRCVEHBITNSDGAC") == 1


def test_case55():
    assert longestCommonSubstring.longestCommonSubstringDP("EIYSBMRNOQSSFVOYXKEGLMAYGFG", "IHQZNAZGDMZQCPIUUDJ") == 1
