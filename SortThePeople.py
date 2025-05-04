# 2418. Sort the People
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # for i in range(len(names)-1, 0, -1):
        #     isSwapped = False
        #     for j in range(i):
        #         if heights[j]<heights[j+1]: # Descending order
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        #             names[j], names[j+1] = names[j+1], names[j]
        #             isSwapped = True
        #     if not isSwapped: break
        # return names
        return [n for h,n in sorted(zip(heights, names), reverse=True)]