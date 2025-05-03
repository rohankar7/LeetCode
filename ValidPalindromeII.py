# 680. Valid Palindrome II
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def plaindromeRange(i, j):
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return plaindromeRange(l+1, r) or plaindromeRange(l, r-1)
            l += 1
            r -= 1
        return True