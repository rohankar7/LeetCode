# 599. Minimum Index Sum of Two Lists
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash = {}
        minVal = len(list1)+len(list2)
        for i in range(len(list1)):
            if list1[i] in list2:
                commonIndex = list2.index(list1[i])+i
                hash[list1[i]] = hash.get(list1[i], commonIndex)
                minVal = min(minVal, commonIndex)
        outList = []
        for k,v in hash.items():
            if v==minVal:
                outList.append(k)
        return outList