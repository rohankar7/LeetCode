# 3407. Substring Matching Pattern
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        start, end = p.split("*")
        startIndex = s.find(start)
        if startIndex != -1 and s[startIndex+len(start):].find(end)!=-1: return True
        return False