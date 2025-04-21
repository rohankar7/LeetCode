# 409. Longest Palindrome
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        size = 0
        addedOdd = False
        for i in s:
            if hashmap.get(i)==None:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        for i in hashmap.values():
            if (i%2==0):
                size += i
            else:
                size += i-1
                addedOdd = True
        if addedOdd:
            size += 1
        return size