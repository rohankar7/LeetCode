# 459. Repeated Substring Pattern
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if (len(s)%2==0):
            ss = s+s
            print(ss)
            print(ss[len(s)//2:-len(s)//2])
            if (ss[len(s)//2:-len(s)//2]==s):
                return True
        return False