# 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        if n==1: return 1
        l = []
        for i in range(n):
            if i == 0: l.append(0)
            elif i == 1 or i == 2: l.append(1)
            else: l.append(sum(l[-3:]))
        return sum(l[-3:])