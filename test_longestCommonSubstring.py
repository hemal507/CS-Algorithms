import longestCommonSubstring


def test_case1():
    assert longestCommonSubstring.longestCommonSubstring("abcdxyz", "xyzabcd") == 4


def test_case2():
    assert longestCommonSubstring.longestCommonSubstring("zxabcdezy", "yzabcdezx") == 6


def test_case3():
    assert longestCommonSubstring.longestCommonSubstring("ABC", "ABCD") == 3


def test_case4():
    assert longestCommonSubstring.longestCommonSubstring("ABCD", "ABC") == 3


def test_case5():
    assert longestCommonSubstring.longestCommonSubstring("ABCDGH", "ACDGHR") == 4


def test_case6():
    assert longestCommonSubstring.longestCommonSubstring("ABC", "AC") == 1


def test_case7():
    assert longestCommonSubstring.longestCommonSubstring(
        "LRBBMQBHCDARZOWKKYHIDDQSCDXRJMOWFRXSJYBLDBEFSARCBYNECDYGGXXPKLORELLNMPAPQFWKHOPKMCO",
        "QHNWNKUEWHSQMGBBUQCLJJIVSWMDKQTBXIXMVTRRBLJPTNSNFWZQFJMAFADRRWSOFSBCNUVQHFFBSAQXWPQCAC") == 2


def test_case8():
    assert longestCommonSubstring.longestCommonSubstring("CHZVFRKMLNOZJK",
                                                         "PQPXRJXKITZYXACBHHKICQCOENDTOMFGDWDWFCGPXIQVKUYTDLCGDEWHTACIOHORDTQKVWCSGSPQOQMSBOAGUWN") == 1


def test_case9():
    assert longestCommonSubstring.longestCommonSubstring(
        "QXNZLGDGWPBTRWBLNSADEUGUUMOQCDRUBETOKYXHOACHWDVMXXRDRYXLMNDQTUKWAGMLEJUUKWCIBXU",
        "BUMENMEYATDRMYDIAJXLOGHIQFMZHLVIHJOUVSUYOYPAYULYEI") == 2


def test_case10():
    assert longestCommonSubstring.longestCommonSubstring(
        "OTEHZRIICFSKPGGKBBIPZZRZUCXAMLUDFYKGRUOWZGIOOOBPPLEQLWPHAPJNADQHDCNVWDTXJBMYPPPHAUXNSPUSGDHIIXQMBF",
        "JXJCVUDJSUYIBYEBMWSIQYOYGYXYMZEVYPZV") == 2


def test_case11():
    assert longestCommonSubstring.longestCommonSubstring("GEBEOCFUFTSXDIXTIGSIEEHKCHZ", "DFLILRJQFNXZ") == 1


def test_case12():
    assert longestCommonSubstring.longestCommonSubstring("RSVBSPK",
                                                         "YHSENBPPKQTPDDBUOTBBQCWIVRFXJUJJDDNTGEIQVDGAIJVWCYAUBWEWPJVYGEHLJXEPBPIWUQZDZU") == 2


def test_case13():
    assert longestCommonSubstring.longestCommonSubstring("UBZVAFSPQPQ", "WUZIF") == 1


def test_case14():
    assert longestCommonSubstring.longestCommonSubstring(
        "VYDDWYVVBURCZMGYJGFDXVTNUNNESLSPLWUIUPFXLZBKNHKWPPANLTCFIRJCDDSOZOYVEGURFW", "CSFMOXEQMRJOWRGHWLKOBMEAHK") == 2


def test_case15():
    assert longestCommonSubstring.longestCommonSubstring(
        "CNAEHHSVEYMQPXHLRNUNYFDZRHBASJEUYGAFOUBUTPNIMUWFJQSJXVKQDORXXVRWCTDSNEOGVBPKXLPGDIRBFC",
        "RIQIFPGYNKRREFXSNVUCFTPWCTGTWMXNUPYCFGCU") == 3


def test_case16():
    assert longestCommonSubstring.longestCommonSubstring("NUBLMOIITNCKLEFSZBEX",
                                                         "RAMPETVHQNDDJEQVUYGPNKAZQFRPJVOAXDPCWMJOBMSKSKFOJNEWXGXNNOFWLTWJWNNVBWJCKDMEOUUZHYVHGVWUJBQX") == 2


def test_case17():
    assert longestCommonSubstring.longestCommonSubstring("ITCVOGRAIDDVHRRDSYCQHKLEEWHXTEMBAQWQW",
                                                         "PQHSUEBNVFGVJWDVJJAFQZZXLCXDZNCQGJLAPOPKVXFGVICETCMKBLJOPGT") == 2


def test_case18():
    assert longestCommonSubstring.longestCommonSubstring(
        "VHBGSDVIVHESNKQXMWRQIDRVMHLUBBRYKTHEYENTMROBDEYQCRGLUAIIHVEIXWJJRQOPUBJGUXHX",
        "DIPFZWSWYBGFYLQVJZHARVRLYAUUZDRCNJKPHCLFFRKEECBPDIPUFHIDJCXJHRNXCXMJCXOHQANXDRMGZEB") == 2


def test_case19():
    assert longestCommonSubstring.longestCommonSubstring("LMWPMHWDVTHSFQUEEEXGRUJIGSKMVRZGFWVRFTWAPDT",
                                                         "UTPBZTYGNSRXAJJNGCOMIKJZSDWSSZNOVDRUYPCNJULKFUZMXNAFAMESPCKJCAZXDRTDGYRQSCCZYBN") == 2


def test_case20():
    assert longestCommonSubstring.longestCommonSubstring("QCQCJITLVCNVBMASIDZ",
                                                         "GWRAATZZWPWMFBFJKNCVKELHHZJCHPDNLUNMPPNLGJZNKEWWUYSGEFONEXPM") == 1


def test_case21():
    assert longestCommonSubstring.longestCommonSubstring(
        "BAOPMDGZQMKQZXUVTQVNXBSLQZKGLZAMZPDNSJOLVYBWXXTTQOGNRBAIAKQLLSZKHF",
        "ZCONNMOQKLPEEFSNSMOUWQHODSGCFOHESYSHMGXWTOAYUVNOJDJFTQTWKBAPRIUJIMQWSPSLGVLCSAQBDBGWTBSEETTWDNFNBY") == 2


def test_case22():
    assert longestCommonSubstring.longestCommonSubstring(
        "PDJXYUZQXSTATBZPCTTHOOFREMGFKRBCVKZVGBOFTHGOJHDNAYWPNBITORAAIBEDNEZWFPDAWLOHSSVTQ", "TKFVSYLJZLUCQ") == 1


def test_case23():
    assert longestCommonSubstring.longestCommonSubstring(
        "WYQDNTDMFRTZLQSEKEJHZKSKLFEPXCHVCZYSVDGCXBBISWMEAYLZIFKTMOIKSSFXTGPOJXQIYSRSQFWQDJQNQCGDQRNLLUI",
        "EAZVMWNUUFNNXVLOYVGMLIUQANDLYAVFAUAOSNLNVACSVPIUMOIAWCQXSWKQWGXYAZNTNAIKAMEYBNUQBCQAGGXACHRYNQXQQM") == 3


def test_case24():
    assert longestCommonSubstring.longestCommonSubstring("OTPQHVOKIIAMMQMVXJVBSOA",
                                                         "IFZYXNJCBERRNMIXXSYJHOVENGBPYQRIXQGWDRYGXRXKFHICAINHWILKQMBPESZDIGZNZ") == 2


def test_case25():
    assert longestCommonSubstring.longestCommonSubstring("ZQSJWATYCBMJAWWMNINEPFDUPLUCLTXMKPV",
                                                         "GRRGTUSEURAGELTKCAPWPBQROMQAWIX") == 2


def test_case26():
    assert longestCommonSubstring.longestCommonSubstring("QKVLFBHWCOCPJMRMBPBEGVSULUQTUUVKESVJTDHVTJMEXFQBVUFDPAXCWN",
                                                         "WQJTBPLYZEDICWSODPWTQRPYUEARHWGFNPAQELOFRSOTQIKTXIPQZ") == 2


def test_case27():
    assert longestCommonSubstring.longestCommonSubstring("VLQMUOUBBJBRPMIXFCLBSTNOSVDKUJCPWSDQHXRKIUEZIO",
                                                         "WOQJPIECWXXBJTNMKJGNCPMVAUQGTAUSOKBFUGJTFIUQBJCLVLAZAMUCIMICNEWDOX") == 2


def test_case28():
    assert longestCommonSubstring.longestCommonSubstring("FUEMDADGKHUFSUEVJAXRNIVCORHFRQQWNUJQU", "O") == 1


def test_case29():
    assert longestCommonSubstring.longestCommonSubstring("VSLQPRLYSKRHUNLJGSOXLEUYYFQU",
                                                         "TOZQHMGYETYYEPFAESJLKZIVDEVDLLYGAZXJNDJRXHRDYYDDQNQDOAYSHWXSHXZJYWUMBFFAMXDNXJQOYIRMIR") == 2


def test_case30():
    assert longestCommonSubstring.longestCommonSubstring("NEKXDLICJFQKKVNXUQMSZCIXMZKWSQOIWYFALP",
                                                         "EUUUGFRTEOMQINUQNIRXELP") == 2


def test_case31():
    assert longestCommonSubstring.longestCommonSubstring("OSAODQSZKOGRFBXTNPDBLTQTMPYYEQTUJUIOKCOWSWQYXN",
                                                         "TNDXQQSGKHVIHBAAWJUGAGLODDKTDJIZYNYOESU") == 2


def test_case32():
    assert longestCommonSubstring.longestCommonSubstring(
        "RYITYJRIFXIMKYROKKTVUSUIQIOJFCKYATRYEKIJKSVUSOKCYEAVWUFPCTAJXKIXDBXJMITWCQQX",
        "FBBFHBADVFUAAUJXFRWKVUUHEPDIFVFKYHSFIULEA") == 2


def test_case33():
    assert longestCommonSubstring.longestCommonSubstring("AAPAHJWTESPLWEQFMNMYMTQ", "RELEIN") == 1


def test_case34():
    assert longestCommonSubstring.longestCommonSubstring("PMFPVOMQUEGHDMXKYNWXZQNSWAXGNJWDXBUUSGKMNQWQDVADIW",
                                                         "AHOQAKQZQGKMLHQFDIMNWZGSPLOROWNPGEHIOXHHFRVQALWDTKSSLY") == 3


def test_case35():
    assert longestCommonSubstring.longestCommonSubstring(
        "JATAXGPDMYLDXUKDNFTPRRUMBMEMLROWRHWOQNTCLGHLCRORZHGSBAECPLPCCDYVNXMDMFHAOPLQ",
        "IZKHIQBJTIMITDKXIKSXJECWMKWABHSL") == 2


def test_case36():
    assert longestCommonSubstring.longestCommonSubstring("VQVWCQEQAZTKYDWRBGXDCJPALSHGEPKZHHVLXCBXDWJCCGTDOQIS",
                                                         "CYSPQZVUQIVZPTLPVOOYNYAPGVSWOAOSAGHRFFNXNJYEELTZAIZNIC") == 2


def test_case37():
    assert longestCommonSubstring.longestCommonSubstring("ZWKNWYHZGPQLWFKJQIPUUJVWTXLBZNRYJDOHBVGHMYUIGGTYQJTMUQ",
                                                         "INNTQMIHNTKDDNALWNMSXSATQQELDACNNPJFERMRNYUQNWBJJPDJHDEAVKNYKPOXHX") == 2


def test_case38():
    assert longestCommonSubstring.longestCommonSubstring(
        "QQEDQAVDWZOIORRWWXYRHLSRDGQKDUVTMZZCZUFVTVFIOYGKVEDERVVUDNEGHB",
        "CTCBXDXEZRZGBPFHZANFFECCBGQFMZJQTLRSPPXQIYWJOBSPEFUJLXNMDDURDDIYOBQ") == 2


def test_case39():
    assert longestCommonSubstring.longestCommonSubstring(
        "PVCOULCVDRZKMKWLYIQDCHGHRGYTZDNOBQCVDEQJYSTMEPXCANIEWQMOXKJWPYMQORLUXEDVYWHCOGH", "OT") == 1


def test_case40():
    assert longestCommonSubstring.longestCommonSubstring("SFGIESTCKRPAIGOCFUFBUBIYRRFFMWAEEIMIDFNNZCPHKFL", "PB") == 1


def test_case41():
    assert longestCommonSubstring.longestCommonSubstring("VTDWLUDS",
                                                         "GAUNGFZOIHBXIFOPRWCJZSDXNGTACWTJYPWEUXVEGYBOGSFXQHIP") == 1


def test_case42():
    assert longestCommonSubstring.longestCommonSubstring(
        "MPUFPXCKICAGHUFCZMACCGWIGMRQCTEQKBWBAAMICOQLIVNJJOOMWKUCZNVDGZTQA", "RSARGKWUAHEYVOHLETJQPO") == 1


def test_case43():
    assert longestCommonSubstring.longestCommonSubstring("JSLKOELFYNZEAVAACEAZUIMYDYPVMGYXBLHPPUUNK",
                                                         "TTKQTMVANUUVJVAHMVVUV") == 2


def test_case44():
    assert longestCommonSubstring.longestCommonSubstring("HZKYWHMGCHQVDCQDPMZMXWNEIKZFGTANTNLPWZ",
                                                         "VAHNVKPLPFAOTXNGEXRFCZZDMUSZLOBIOKVKWKXLRXBLVOTZOMEQLFTXZLZKBCSQMNCIAZVRZYEUPYVDKBTWHPVGCWTEYLWKB") == 2


def test_case45():
    assert longestCommonSubstring.longestCommonSubstring("BXRUWSZSHXPM",
                                                         "JRHFAWDIBZBFYPDKSBHTAAPZSORBNJPZCXECVJMWJQDJHGVZJCUKFJJZACBPNSOPPVTLEI") == 2


def test_case46():
    assert longestCommonSubstring.longestCommonSubstring("YNYFVUEFYYRDJADJEGBSY",
                                                         "PJOMFBRNKILZHSVBWCZWTDFVIRBOSVMJFCYMDRZQZKPGEMJAOJYJOFEYWIMQDAC") == 2


def test_case47():
    assert longestCommonSubstring.longestCommonSubstring("AWITXYSJQZNCIPTTNC", "JTJHRTVKW") == 1


def test_case48():
    assert longestCommonSubstring.longestCommonSubstring("JBQHJJFKBOACCENRXIHCSANBTGXDCTTNUJVFSCRWQTYUYNMXWVBQXORQ",
                                                         "UOWZHPMDZJLR") == 1


def test_case49():
    assert longestCommonSubstring.longestCommonSubstring("NCYOYWBMVZHXPENHVIVTHFIVKHFXBQAQUYETWIFTHNSXRGGOQBHXIQSVZ",
                                                         "ZSCQUTMSZF") == 2


def test_case50():
    assert longestCommonSubstring.longestCommonSubstring(
        "NMTAEQTMYKCBRZKJUHLTZNLUIYOKFHVSTOUZGQMEAOGRQSDMZOHYDTUOTJYYST", "TLKNMQDYVDPBX") == 2


def test_case51():
    assert longestCommonSubstring.longestCommonSubstring(
        "ATUQASTVPHOAHPSDIFNXRFBQAGHDFOYHHSXHNTDCCTCMIUPQZEQSJRKMZRPHFOOOIOYVJDXNWBZHVQZWUPRGIBSITJPAZFRIT",
        "PFESFSQGR") == 1


def test_case52():
    assert longestCommonSubstring.longestCommonSubstring("KXCGMTMVVGFQQWSPD",
                                                         "JXZADDUKVLQPKUZJZHWSUTPCAFSYAIBJHAMMEGWBTPQELRNKBLDXGUZGCSEC") == 2


def test_case53():
    assert longestCommonSubstring.longestCommonSubstring("NLIZYOGWQZLIFXCTHDGMANJZTLTANVIAJSCHHKDXLRFROHMXMSMMHVODIH",
                                                         "DVFNXOFBXMLCLXVROJACJPWXBEURHCBMZGZWWGYVTLZEIVXYGAAPPZOSDIKKMLWLTXIRDIOYTNFEIEEPEH") == 2


def test_case54():
    assert longestCommonSubstring.longestCommonSubstring("GVQJFAVSNTFIQNBVXPUTCZZNFDCMKKHSHXDNZYHORMWJ",
                                                         "CXFBOBWRCVEHBITNSDGAC") == 1


def test_case55():
    assert longestCommonSubstring.longestCommonSubstring("EIYSBMRNOQSSFVOYXKEGLMAYGFG", "IHQZNAZGDMZQCPIUUDJ") == 1
