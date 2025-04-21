# 257. Binary Tree Paths
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def rootToLeaf(node, path):
            if node==None:
                return
            path += f"->{node.val}" if len(path)>0 else f"{node.val}"
            rootToLeaf(node.left, path)
            rootToLeaf(node.right, path)
            if node.right==None and node.left==None:
                paths.append(path)
        rootToLeaf(root, "")
        return paths