def knapsackLight2(w1, w2, m):
    if m >= w1 + w2 :
        return 'both'
    elif m < w1 and m < w2 :
        return 'none'
    elif m >= w1 and m >= w2 :
        return 'either'
    elif m >= w1 and m < w2 :
        return 'first'
    else :
        return 'second'


