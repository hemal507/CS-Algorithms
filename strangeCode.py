def strangeCode(s, e):
    code=[]
    while s < e-1 :
        s += 1
        e -= 1
        if len(code) == 0 or code[-1] == 'b' :
            code.append('a')
        else :
            code.append('b')
    return ''.join(code)  
