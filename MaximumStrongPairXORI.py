# 2932. Maximum Strong Pair XOR I
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        return max([(i^j) for j in nums for i in nums if abs(i-j) <= min(i,j)])