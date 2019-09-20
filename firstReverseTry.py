def firstReverseTry(arr):
    if len(arr) == 0 or len(arr) == 1 :
        return arr
    
    return [arr[-1]] + arr[1:-1] + [arr[0]]
