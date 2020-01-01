def fractionComparison(a,b) :
    r=a[0]/float(b[0]) - a[1] / float(b[1])
    return '=' if r == 0 else '<' if r < 0 else '>'
