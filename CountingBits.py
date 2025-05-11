# 338. Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        # arr = []
        # for i in range(n+1):
        #     arr.append(sum([1 for j in bin(i)[2:] if j=="1"]))
        # return arr
        return [i.bit_count() for i in range(n+1)]