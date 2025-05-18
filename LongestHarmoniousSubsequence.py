# 594. Longest Harmonious Subsequence
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        maxSize = 0
        k = list(hash.keys())
        v = list(hash.values())
        for i in range(len(hash)-1):
            if k[i+1] == k[i] + 1:
                maxSize = max(maxSize, v[i]+v[i+1])
        return maxSize