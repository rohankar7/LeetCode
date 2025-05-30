# 1331. Rank Transform of an Array
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hash = {}
        index = 1
        for i in sorted(arr):
            if hash.get(i)==None:
                hash[i] = index
                index += 1
        return [hash[i] for i in arr]