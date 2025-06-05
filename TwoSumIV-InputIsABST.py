# 653. Two Sum IV - Input is a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash = {}
        def inorder(node):
            if not node: return
            hash[node.val] = hash.get(node.val, 0) + 1
            inorder(node.left)
            inorder(node.right)
        inorder(root)
        for key, val in hash.items():
            if k-key in hash.keys():
                if k-key==key and val<2: continue
                else: return True
        return False