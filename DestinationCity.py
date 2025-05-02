# 1436. Destination City
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dests = [path[1] for path in paths]
        sources = [path[0] for path in paths]
        for d in dests:
            if d not in sources: return d
        return ""