# 3210. Find the Encrypted String
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        if len(set(s))==1 or len(s)==1: return s
        copy = ""
        for i in range(len(s)):
            copy += s[(i+k)%len(s)]
        return copy