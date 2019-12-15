checkIncreasingSequence = lambda s : all([x<y for x,y in zip(s[:-1],s[1:])])

checkIncreasingSequence = lambda s : s == sorted(set(s))
