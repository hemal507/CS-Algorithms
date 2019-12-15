checkIncreasingSequence = lambda s : all([x<y for x,y in zip(s[:-1],s[1:])])


