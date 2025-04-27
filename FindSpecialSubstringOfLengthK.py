# 3456. Find Special Substring of Length K
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s)-k+1):
            if s[i:i+k]==s[i]*k:
                if (i-1>=0 and s[i-1]!=s[i]) or (i-1<0):
                    if (i+k<len(s) and s[i+k]!=s[i]) or i+k>=len(s):
                        return True
        return False