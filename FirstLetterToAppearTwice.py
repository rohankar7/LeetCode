# 2351. First Letter to Appear Twice
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash = {}
        for i in range(len(s)):
            if s[i] not in hash:
                hash[s[i]] = [i]
            else:
                hash[s[i]].append(i)
        smallest = ""
        smallestIndex = len(s)-1
        for k,v in hash.items():
            if len(v)>1 and smallestIndex>=v[1]:
                smallestIndex = v[1]
                smallest = k
        return smallest