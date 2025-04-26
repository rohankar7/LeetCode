# 3461. Check If Digits Are Equal in String After Operations I
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            sum = ""
            for i in range(len(s)-1):
                sum += str((int(s[i])+int(s[i+1]))%10)
            s = sum
        return s[0]==s[1]