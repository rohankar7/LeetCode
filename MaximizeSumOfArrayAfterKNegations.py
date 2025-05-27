# 1005. Maximize Sum Of Array After K Negations
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            nums.sort()
            nums[0] *= -1
        return sum(nums)