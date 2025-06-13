# 3423. Maximum Difference Between Adjacent Elements in a Circular Array
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max([abs(nums[i]-nums[(i+1)%len(nums)]) for i in range(len(nums))])