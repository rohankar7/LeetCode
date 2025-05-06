# 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ""
        for i, j in zip(word1, word2):
            final += i+j
        a,b = len(word1),len(word2)
        if a>b: final += word1[b:]
        elif a<b: final += word2[a:]
        return final