# 1374. Generate a String With Characters That Have Odd Counts
class Solution:
    def generateTheString(self, n: int) -> str:
        return ("a"*(n-1) + "b") if n%2==0 else ("a"*n)