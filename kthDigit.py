def kthDigit(n, k):
    l=len(`n`)
    if l > 0 and k <= l:
        return int(`n`[k-1])
    return -1

kthDigit = lambda n, k : int(`n`[k-1]) if len(`n`) > 0 and k <= len(`n`) else -1

