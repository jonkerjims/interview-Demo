# -*- coding: utf-8 -*-
def threeSum(nums):
    nums.sort()
    print(nums)
    length = len(nums)

    res = set()
    for i in range(length):
        target = -nums[i]
        right = length - 1

        left = i + 1
        while left < right:
            Sum = nums[left] + nums[right]
            if Sum == target:
                # print(nums[i], nums[left], nums[right])
                res.add(str([nums[i], nums[left], nums[right]]))
                left += 1
                right -= 1
            elif Sum < target:
                left += 1
            else:
                right -= 1
    return list(str(i) for i in res)
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))