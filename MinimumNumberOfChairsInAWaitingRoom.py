# 3168. Minimum Number of Chairs in a Waiting Room
class Solution:
    def minimumChairs(self, s: str) -> int:
        people, minChairs = 0, 0
        for i in s:
            if i == "E":
                people += 1
                if people > minChairs: minChairs += 1
            else: people -= 1
        return minChairs