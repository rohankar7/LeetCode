# 563. Binary Tree Tilt
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def postOrder(node)->int:
            if node==None: return 0
            lChild = postOrder(node.left)
            rChild = postOrder(node.right)
            self.sum += abs(lChild-rChild)
            return node.val+lChild+rChild
        postOrder(root)
        return self.sum