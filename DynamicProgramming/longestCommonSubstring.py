def longestCommonSubstring(s, t):
    r=0
    for i in range(len(s)) :
        for j in range(i+1,len(s)+1) :
            n = s[i:j]
            print(n)
            if n in t and len(n) > r :
                r=j-i
    return r


def longestCommonSubstring(s, t):
    if len(t) > len(s):
        t, s = s, t
    l = len(t)
    if t in s:
        return l
    if t[:-1] in s:
        return l - 1
    m = 0
    for i in range(min(l, 10000)):
        while t[i:i + m + 1] in s and i + m < l:
            m += 1
    return m

def longestCommonSubstringDP(a, b) :
    x = len(a)
    y = len(b)
    lcs = [ [None for i in range(y+1)] for j in range(x+1) ]
    for i in range(x+1) :
        for j in range(y+1) :
            if i == 0  or j == 0:
                lcs[i][j] = 0
            elif a[i-1] == b[j-1] :
                lcs[i][j] = lcs[i-1][j-1] + 1
            else :
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
    return lcs[x][y]


print(longestCommonSubstringDP("ABCDGH", "ACDGHR"))
