def quicksort(arr):
    if len(arr) <= 1:
        return arr
    print('List : ', arr)
    pivot = arr[len(arr) // 2]
    print('Pivot: ', pivot)
    left = [x for x in arr if x < pivot]
    print('left: ', left)
    middle = [x for x in arr if x == pivot]
    print('middle: ',middle)
    right = [x for x in arr if x > pivot]
    print('Right: ',right)
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,6,6,6,2,1]))
