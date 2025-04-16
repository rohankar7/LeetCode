# 696. Count Binary Substrings
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, current = -1, 0
        count0, count1 = 0, 0
        for i in range(len(s)):
            if s[i]==0:
                count0 += 1
            else:
                count1 += 1
            prev = current
            current = i
            if s[prev] != s[current]:
                print("")