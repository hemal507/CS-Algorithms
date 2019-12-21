def knapsackLight(v1, w1, v2, w2, maxW):
    if w1 + w2 <= maxW:
        return v1 + v2
    if min(w1, w2) > maxW:
        return 0
    if w1 <= maxW and (v1 >= v2 or w2 > maxW):
        return v1
    return v2

