# 530. Minimum Absolute Difference in BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l = []
        def minDiff(node):
            if node==None: return
            l.append(node.val)
            minDiff(node.left)
            minDiff(node.right)
        minDiff(root)
        l.sort()
        minimum = float("inf")
        for i in range(1, len(l)):
            minimum = min(l[i]-l[i-1], minimum)
        return minimum