# 748. Shortest Completing Word
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = "".join([i.lower() for i in licensePlate if i.isalpha() ])
        w = []
        for word in words:
            temp = word
            flag = False
            for char in licensePlate:
                if char in word:
                    word = word[:word.find(char)] + word[word.find(char)+1:]
                else:
                    flag = True
                    break
            if flag: continue
            w.append(temp)
        short = len(w[0])
        shortInd = 0
        for i in range(1, len(w)):
            print(shortInd)
            if short>len(w[i]):
                short = len(w[i])
                shortInd = i
        return w[shortInd]