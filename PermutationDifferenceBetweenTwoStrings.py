# 3146. Permutation Difference between Two Strings
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(i - t.find(v)) for i,v in enumerate(s))