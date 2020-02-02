def ballsRearranging(balls):
    m = min(balls)
    x = max(balls)
    l = len(balls)
    c = 0
    m = 0
    for i in range(m + 1, x):
        n = sum([1 for x in range(i, i + l) if x in balls])
        if c < n:
            c = n
            m = l - n
    return m