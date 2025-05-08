# 151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i.strip() for i in s.split(" ")[::-1] if i != ""])