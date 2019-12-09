def isSmooth(arr):
    l = len(arr)
    m=arr[0]
    if l % 2 != 0 :
        m = arr[l/2]
    else :
        m = arr[l/2] + arr[(l/2)-1]
    return True if arr[0] == arr[-1] == m else False
    


