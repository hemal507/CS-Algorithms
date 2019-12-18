def reduceString(s):
    while len(s) > 1 and s[0] == s[-1]:
        s = s[1:-1]
    return '' if len(s) < 2 else s


print(reduceString("abacaba"))
print(reduceString("12133221"))
print(reduceString(""))
