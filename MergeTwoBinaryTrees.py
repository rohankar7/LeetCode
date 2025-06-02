# 617. Merge Two Binary Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not t1 and not t2: return
        elif not t1: return t2
        elif not t2: return t1
        mergedTree = TreeNode(t1.val + t2.val)
        mergedTree.left = self.mergeTrees(t1.left, t2.left)
        mergedTree.right = self.mergeTrees(t1.right, t2.right)
        return mergedTree