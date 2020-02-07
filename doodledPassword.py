from collections import deque


def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    map(lambda i, j: i.rotate(j), res, range(n, 0, -1))
    return [list(d) for d in res]
