def missingNumber(arr) :
    return ([x for x in range(1, len(arr) + 1) if x not in arr] + [0])[0]

print(missingNumber([3,1,0]))
print(missingNumber([0]))