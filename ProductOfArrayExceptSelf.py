# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = prod(nums)
        count = 0
        nonZeroProd = 1
        for i in nums:
            if i == 0: count += 1
            else: nonZeroProd *= i
        return [p//i if i != 0 else 0 if count > 1 else nonZeroProd for i in nums]