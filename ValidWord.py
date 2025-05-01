# 3136. Valid Word
class Solution:
    def isValid(self, word: str) -> bool:
        cons, vowel = False, False
        if word.isalnum() and len(word)>=3:
            for i in word:
                if i in "aeiouAEIOU": vowel = True
                elif i.isalpha(): cons = True
        return cons and vowel