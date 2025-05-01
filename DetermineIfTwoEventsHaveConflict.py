# 2446. Determine if Two Events Have Conflict
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        a,b = event1[0].split(":")
        c,d = event1[1].split(":")
        e, f = event2[0].split(":")
        g, h= event2[1].split(":")
        return (a<g or (a==g and b<=h)) and (c>e or (c==e and d>=f))