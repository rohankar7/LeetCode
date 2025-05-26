# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i,w in enumerate(sentence.split(" ")):
            if w[:len(searchWord)]==searchWord: return i+1
        return -1