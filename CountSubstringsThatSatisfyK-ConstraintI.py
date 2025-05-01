# 3258. Count Substrings That Satisfy K-Constraint I
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        subsetCount = 0
        subsets = []
        for i in range(len(s)):
            for j in range(len(s)-i+1):
                if len(s[i:i+j])>0:
                    subsets.append(s[i:i+j])
                    count0, count1 = 0, 0
                    for num in s[i:i+j]:
                        if num=="0": count0 += 1
                        else: count1 += 1
                    print(s[i:i+j])
                    if (count0 <= k) or (count1 <= k): subsetCount += 1
        return subsetCount