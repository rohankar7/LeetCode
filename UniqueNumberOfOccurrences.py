# 1207. Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = {}
        for i in arr: hash[i] = hash.get(i, 0) + 1
        return len(hash.values()) == len(set(hash.values()))