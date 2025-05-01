# 3174. Clear Digits
class Solution:
    def clearDigits(self, s: str) -> str:
        i = 1
        while len(s)>1:
            if s[i].isnumeric() and s[i-1].isalpha():
                s = s[:i-1] + s[i+1:]
                i = i-2 if (i-2 >= 0) else 0
            else: i += 1
            if i==len(s): break
        return s