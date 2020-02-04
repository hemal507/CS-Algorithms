"""
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
"""

def ballsRearranging(balls):
    s = sorted(balls)
    i = 0
    for a in s:
        i += a - s[i] >= len(s)
    return i

print(ballsRearranging([6, 4, 1, 7, 10]))