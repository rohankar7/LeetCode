# 3442. Maximum Difference Between Even and Odd Frequency I
class Solution:
    def maxDifference(self, s: str) -> int:
        hash = {}
        for char in s:
            if hash.get(char)==None: hash[char] = 1
            else: hash[char] += 1
        maxOdd, minEven = 0, len(s)
        for v in hash.values():
            if v%2==0: minEven = min(minEven, v)
            else: maxOdd = max(maxOdd, v)
        return (maxOdd - minEven)