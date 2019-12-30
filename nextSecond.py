def nextSecond(currentTime):
    h, m, s = currentTime
    s += 1
    m += s / 60
    s %= 60
    h += m / 60
    m %= 60
    h %= 24
    return [h, m, s]


