# 1408. String Matching in an Array
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return list(set([j for j in words for w in words if w!=j and w in j]))