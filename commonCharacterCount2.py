def commonCharacterCount2(s) :
    t = set([x for y in s for x in y])
    # print(t)
    return sum( [ min(i.count(c) for i in s ) for c in t ] )\

print(commonCharacterCount2(["aabcc", "adcaa", "acdba"]))