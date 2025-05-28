# 1051. Height Checker
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(1 for i,j in zip(sorted(heights),heights) if i!=j)