def replaceMiddle(arr):
    if len(arr) % 2 == 1 :
        return arr
    p = len(arr)/2
    return arr[:p-1] + [ arr[p] + arr[p-1] ] + arr[p+1:]


