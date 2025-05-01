# 3216. Lexicographically Smallest String After a Swap
class Solution:
    def getSmallestString(self, s: str) -> str:
        for i in range(len(s)-1):
            a, b = int(s[i]), int(s[i+1])
            if (a%2==b%2) and (b<a): return s[:i]+s[i+1]+s[i]+s[i+2:]
        return s