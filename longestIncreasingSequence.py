def longestIncreasingSequence(a) :
    r=[1] * len(a)
    for i in range(1,len(a)) :
        for j in range(i) :
            if a[j] < a[i] and r[i] < r[j] + 1 :
                r[i] = r[j] + 1
    return max(r)
#
# print(longestIncreasingSequence([10, 22, 9,33, 21, 50, 41, 60]))
# print(longestIncreasingSequence([1, -1, -2, -99]))
# print(longestIncreasingSequence([-99, -4, -1, -1, 0, 99, 800]))
# print(longestIncreasingSequence([-99, -4, -1, 0, 99, 800]))