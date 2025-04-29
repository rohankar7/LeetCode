# 3340. Check Balanced String
class Solution:
    def isBalanced(self, num: str) -> bool:
        total = 0
        for i in range(len(num)): # Subtract for even positions and Add for odd positions
            total += int(num[i])*(-1 if i%2==0 else 1)
        return total==0