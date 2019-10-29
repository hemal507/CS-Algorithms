import htmlEndTagByStartTag

def test_case1() :
	assert htmlEndTagByStartTag.htmlEndTagByStartTag("<button type='button' disabled>") == "</button>"

def test_case2() :
        assert htmlEndTagByStartTag.htmlEndTagByStartTag("<i>") == "</i>"

def test_case3() :
        assert htmlEndTagByStartTag.htmlEndTagByStartTag("<div id='my_area' class='data' title='This is a test for title on Div tag'>") == "</div>"

def test_case4() :
        assert htmlEndTagByStartTag.htmlEndTagByStartTag("<html>") == "</html>"

def test_case5() :
        assert htmlEndTagByStartTag.htmlEndTagByStartTag("<TABLE border='1'>") == "</TABLE>"

def test_case6() :
        assert htmlEndTagByStartTag.htmlEndTagByStartTag("<li class='test'>") == "</li>"
