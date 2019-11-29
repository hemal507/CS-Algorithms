def isArithmeticProgression(s):
    return all([a-b == s[0]-s[1] for a,b in zip(s[:-1], s[1:])])


