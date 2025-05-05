# 2399. Check Distances Between Same Letters
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i in set(s):
            dist = [j for j,v in enumerate(s) if v==i]
            if dist[1]-dist[0]-1 != distance[ord(i)-97]: return False
        return True