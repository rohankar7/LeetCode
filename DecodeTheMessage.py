# 2325. Decode the Message
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        sample = []
        for i in key:
            if i not in sample and i != " ": sample.append(i)
        hash = {}
        for i in range(len(sample)):
            if sample[i]!=" ": hash[sample[i]] = hash.get(sample[i], chr(i+97))
        return "".join([hash[i] if i != " " else " " for i in message])