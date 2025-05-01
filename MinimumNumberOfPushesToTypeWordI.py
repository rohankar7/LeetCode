# 3014. Minimum Number of Pushes to Type Word I
class Solution:
    def minimumPushes(self, word: str) -> int:
        count, mul = 0, 0
        for i in range(len(word)):
            if i%8==0: mul += 1
            count += mul
        return count