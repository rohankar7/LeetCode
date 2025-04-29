# 3438. Find Valid Pair of Adjacent Digits in String
class Solution:
    def findValidPair(self, s: str) -> str:
        hash = {}
        for char in s:
            hash[char] = hash.get(char, 0) + 1
        for i in range(len(s)-1):
            a = s[i]
            b = s[i+1]
            if hash[a]==int(a) and hash[b]==int(b) and a!=b: return (a+b)
        return ""