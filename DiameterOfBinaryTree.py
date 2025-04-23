# 543. Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        def inOrder(node)->int:
            if node==None:
                return 0
            l = inOrder(node.left)
            r = inOrder(node.right)
            subsetDiameter = l + r
            self.d = max(self.d, subsetDiameter)
            return 1 + max(l, r)
        inOrder(root)
        return self.d