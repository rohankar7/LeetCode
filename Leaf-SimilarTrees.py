# 872. Leaf-Similar Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafSeq1, leafSeq2 = [], []
        def traverseTree(node, seq):
            if node == None: return
            if node.right==None and node.left==None: seq.append(node.val)
            traverseTree(node.left, seq)
            traverseTree(node.right, seq)
        traverseTree(root1, leafSeq1)
        traverseTree(root2, leafSeq2)
        return leafSeq1 == leafSeq2