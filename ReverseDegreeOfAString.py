# 3498. Reverse Degree of a String
class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0
        asciia = ord('a') + 26
        for i in range(len(s)):
            sum += (asciia-ord(s[i]))*(i+1)
        return sum