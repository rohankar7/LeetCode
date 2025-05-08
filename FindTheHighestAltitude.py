# 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt, sumAlt = 0, 0
        for i in gain:
            sumAlt += i
            maxAlt = max(maxAlt, sumAlt)
        return maxAlt