def arrayTwoCandidates(a, v) :
    s = set()
    for i in a :
        if v - i in s :
            return i, v - i
        s.add(i)

print(arrayTwoCandidates([1,2 ,4, -1, 11, 12, 13, 21, 15, 9, -2], 8))