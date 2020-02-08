def longestCommonSubstring(s, t):
    r=0
    for i in range(len(s)) :
        for j in range(i+1,len(s)+1) :
            n = s[i:j]
            print(n)
            if n in t and len(n) > r :
                r=j-i
    return r


print(longestCommonSubstring("ABCDGH", "ACDGHR"))
