def sumInRange(nums, queries):
    l = len(nums)
    sums = [0] * (l + 1)
    for i in range(l):
        sums[i + 1] = sums[i] + nums[i]

    return sum(sums[y + 1] - sums[x] for x, y in queries) % 1000000007


print(sumInRange([3, 0, -2, 6, -3, 2], [[0, 2], [2, 5], [0, 5]]))
