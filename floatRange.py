from itertools import count, takewhile

def floatRange(start, stop, step):
    gen =takewhile(lambda x : x < stop , count(start=start,step=step))
    return list(gen)

