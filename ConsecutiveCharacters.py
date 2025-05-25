# 1446. Consecutive Characters
class Solution:
    def maxPower(self, s: str) -> int:
        temp = s[0]
        count, maxCount = 0, 0
        for c in s:
            if c==temp: count += 1
            else:
                temp = c
                maxCount = max(maxCount, count)
                count = 1
        return max(maxCount, count)