def houseRobber(nums) :
    current = maximum = 0
    for i in nums:
        current, maximum = maximum, max(current + i, maximum)
    return maximum

print(houseRobber([4, 1, 2, 7, 5, 3, 1]))