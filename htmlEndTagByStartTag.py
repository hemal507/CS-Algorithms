def htmlEndTagByStartTag(startTag):
    s = startTag.split()
    r=''
    if s[0][1] != '/' :
        r = s[0][:1] + '/' + s[0][1:]
    if r[-1] != '>' :
        r += '>'
    return r    

